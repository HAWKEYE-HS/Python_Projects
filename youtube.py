from pytube import YouTube
from hurry.filesize import size
import telebot
import time

video_streams = []
videos = []

TOKEN = "XYTZ"
Bot = telebot.TeleBot(TOKEN)

text = []


def check(message):
    if message.text != '/download':
        return True
    return False
    # Bot.send_message(message.chat.id, message.text)


# def check2(message):
@Bot.message_handler(commands=['start'])
def send(message):
    Bot.send_message(message.chat.id, "/download - Download Video")


@Bot.message_handler(func=check)
def send(message):
    text.append(message.text)
    Bot.send_message(message.chat.id, text[0])


@Bot.message_handler(commands=['download'])
def send(message):
    yt = YouTube(text[0])
    text.clear()
    Bot.send_message(message.chat.id, yt.title)
    for stream in yt.streams.order_by("resolution").filter(progressive=True):
        video_streams.append(stream.resolution)  # Getting resolutions
        videos.append(stream)
    i = 1
    for resolution in video_streams:
        Bot.send_message(message.chat.id, f"{i} : {resolution}")
        Bot.send_message(message.chat.id, f"size : {size(videos[i - 1].filesize)}B")
        i += 1
    Bot.send_message(message.chat.id, "Select a number")
    time.sleep(10)
    choice = int(text[0])
    Bot.send_message(message.chat.id, str(choice))
    if choice <= len(videos):
        videos[choice - 1].download()
    Bot.send_message(message.chat.id, "Video downloaded successfully")
    Bot.send_video(message.chat.id, video=open(f"{yt.title}.mp4", "rb"), supports_streaming=True)


Bot.polling()
