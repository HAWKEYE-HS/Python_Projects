from pytube import YouTube
from hurry.filesize import size
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk

video_streams = []
video_links = []


def one():
    video_links[0].download()
    tmsg.showinfo("Success", "Video Downloaded Successfully")


def two():
    video_links[1].download()
    tmsg.showinfo("Success", "Video Downloaded Successfully")


def three():
    video_links[2].download()
    tmsg.showinfo("Success", "Video Downloaded Successfully")


def download():
    link = text.get()
    win = Toplevel()
    yt = YouTube(link)
    print(yt.title)
    win.title("Video")
    win.geometry("900x300")
    Label(win, text=yt.title, font=("Eras Light ITC", 14, "bold"), fg="green").pack()
    i = 0
    for stream in yt.streams.order_by("resolution").filter(progressive=True):
        video_streams.append(stream.resolution)
        video_links.append(stream)

    for resolution in video_streams:
        print(f"{i} : {resolution}")
        print(f"Size : {size(video_links[i].filesize)}B")
        i += 1
    b1 = Button(win, text=f"{video_streams[0]} : {size(video_links[0].filesize)}B", font="Calibri 12", bg="green",
                fg="white", command=one)
    b1.pack(pady=15)
    b2 = Button(win, text=f"{video_streams[1]} : {size(video_links[1].filesize)}B", font="Calibri 12", bg="green",
                fg="white", command=two)
    b2.pack(pady=15)
    b3 = Button(win, text=f"{video_streams[2]} : {size(video_links[2].filesize)}B", font="Calibri 12", bg="green",
                fg="white", command=three)
    b3.pack(pady=15)
    win.grab_set()


root = Tk()
img = Image.open(r"C:\Users\omdoi\Videos\Captures\Logo.png")
photo = img.resize((100, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(photo)
root.title("Downloader")
root.geometry("400x300")
Label(root, text="YouTube Video Downloader", font="Georgia 16 underline", fg="red", compound=LEFT, image=logo).pack()
text = StringVar()
Label(root, text="Enter a link : ", font="Butterfly 12", fg="purple").pack(pady=14)
link = Entry(root, textvariable=text, bd=3, relief=RAISED, width=40)
link.pack()
Button(root, text="Extract", font="Kalinga 14", bg="green", fg="white", relief=SUNKEN, bd=3, command=download).pack(
    pady=14)

root.mainloop()
