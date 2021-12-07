import telebot
import qrcode
from pyzbar import pyzbar
from PIL import Image
from barcode.writer import ImageWriter
from barcode import Code128

TOKEN = "XYZ"
Bot = telebot.TeleBot(TOKEN)
path = r'C:\Users\colorado.colorado-PC\Documents\2020ENGG_CAP2_CutOff.pdf'
text_qr_code = []
text_bar_code = []


def check(message):
    text = message.text.split()
    if len(text) > 1:
        return True
    return False


@Bot.message_handler(commands=['start'])
def send(message):
    Bot.send_message(message.chat.id, "/scan - to scan QR or Bar Code")
    Bot.send_message(message.chat.id, "/generate - QR Code")
    Bot.send_message(message.chat.id, "/make - generate barcode")


@Bot.message_handler(content_types=["photo"])
def get_photo(message):
    fileID = message.photo[-1].file_id
    file_info = Bot.get_file(fileID)
    downloaded_file = Bot.download_file(file_info.file_path)

    with open("QRCODE.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)


@Bot.message_handler(commands=['scan'])
def scan_content(message):
    img = Image.open("QRCODE.jpg")
    result = pyzbar.decode(img)
    for code in result:
        info = code.data.decode('utf-8')
        Bot.send_message(message.chat.id, info)


@Bot.message_handler(func=check)
def get_text(message):
    if 'qr' in message.text:
        text_qr_code.append(message.text.replace("qr", ""))
        Bot.send_message(message.chat.id, text_qr_code[0])
    else:
        text_bar_code.append(message.text.replace("bar", ""))
        Bot.send_message(message.chat.id, text_bar_code[0])


@Bot.message_handler(commands=['generate'])
def make_qr_code(message):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=10,
                       border=4)
    qr.add_data(text_qr_code[0])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode2.png")
    Bot.send_photo(message.chat.id, photo=open("qrcode2.png", "rb"))
    text_qr_code.clear()


@Bot.message_handler(commands=['make'])
def make_barcode(message):
    with open('barcode.png', 'wb') as f:
        Code128(text_bar_code[0].replace(" ", ""), writer=ImageWriter()).write(f)

    Bot.send_photo(message.chat.id, photo=open("barcode.png", "rb"))
    text_bar_code.clear()


Bot.polling()
