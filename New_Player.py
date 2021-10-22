from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from mutagen.mp3 import MP3
from mutagen import MutagenError
from pygame import mixer
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg


class MusicPlayer(Frame):
    def __init__(self, master, file, tracktype="mp3", *args, **kwargs):
        super().__init__(master)
        self.pack()

        # MusicPlayer's Attributes
        self.master = master
        self.track = None
        self.tracklength = None
        self.player = None
        self.playBut = None
        self.stopBut = None
        self.slider = None
        self.slider_val = None
        self.file = file
        # Call these methods
        self.get_AudioFile(tracktype)
        self.load_AudioFile()
        self.create_Widgets()

    def get_AudioFile(self, tracktype):
        try:
            if tracktype == 'mp3':
                audiofile = self.file
                f = MP3(audiofile)
            else:
                pass
        except MutagenError:
            print("Fail to load audio file ({}) metadata".format(audiofile))
        else:
            tracklength = f.info.length
        self.track = audiofile
        self.tracklength = tracklength

    def load_AudioFile(self):
        player = mixer
        player.init()
        player.music.load(self.track)
        player.music.set_volume(0.25)
        self.player = player

    def create_Widgets(self):
        img = Image.open("Play.jpg")
        img = img.resize((50, 50), Image.ANTIALIAS)
        self.play = ImageTk.PhotoImage(img)
        img2 = Image.open("Pause.jpg")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.pause = ImageTk.PhotoImage(img2)
        img3 = Image.open("Repeat.jpeg")
        img3 = img3.resize((50, 50), Image.ANTIALIAS)
        self.repeat = ImageTk.PhotoImage(img3)
        img4 = Image.open("Fast.png")
        img4 = img4.resize((50, 50), Image.ANTIALIAS)
        self.fast = ImageTk.PhotoImage(img4)
        img5 = Image.open("Back.png")
        img5 = img5.resize((50, 50), Image.ANTIALIAS)
        self.back = ImageTk.PhotoImage(img5)
        img6 = Image.open("Next.png")
        img6 = img6.resize((50, 50), Image.ANTIALIAS)
        self.next = ImageTk.PhotoImage(img6)
        img7 = Image.open("Prev.png")
        img7 = img7.resize((50, 50), Image.ANTIALIAS)
        self.prev = ImageTk.PhotoImage(img7)
        img8 = Image.open("Power.png")
        img8 = img8.resize((50, 50), Image.ANTIALIAS)
        self.power = ImageTk.PhotoImage(img8)
        f = Frame(self)
        self.PowerBut = Button(f, image=self.power, command=exit)
        self.PowerBut.pack(side=LEFT, padx=5, pady=10)
        self.BackBut = Button(f, image=self.back, command=self.Back)
        self.BackBut.pack(side=LEFT, padx=5, pady=10)

        self.PrevBut = Button(f, image=self.prev, command=self.Prev)
        self.PrevBut.pack(side=LEFT, padx=5, pady=10)

        self.playBut = Button(f, image=self.play, command=self.Play)
        self.playBut.pack(side=LEFT, padx=5, pady=10)

        self.nextBut = Button(f, image=self.next, command=self.Next)
        self.nextBut.pack(side=LEFT, padx=5, pady=10)

        self.FastBut = Button(f, image=self.fast, command=self.Fast)
        self.FastBut.pack(side=LEFT, padx=5, pady=10)

        self.repeatBut = Button(f, image=self.repeat, command=self.Repeat)
        self.repeatBut.pack(side=LEFT, padx=5, pady=10)

        f.pack()
        self.slider_val = DoubleVar()
        self.slider = Scale(self, to=self.tracklength, orient=HORIZONTAL, length=700, resolution=0.5, showvalue=True,
                            tickinterval=30, digit=4, variable=self.slider_val, command=self.UpdateSlider)
        self.slider.pack(side=RIGHT)

    def Play(self):
        """Play track from slider location"""
        self.playBut.config(image=self.pause, command=self.Stop)
        update.set("Playing...")
        l.update()
        playtime = self.slider_val.get()
        self.player.music.play(start=playtime)
        self.TrackPlay(playtime)

    def TrackPlay(self, playtime):
        """Slider to track the playing of the track"""
        if self.player.music.get_busy():
            self.slider_val.set(playtime)
            playtime += 1.0
            self.loopID = self.after(1000, lambda: self.TrackPlay(playtime))

    def UpdateSlider(self, value):
        """Move slider position when Scale's trough is clicked or when slider is clicked"""
        if self.player.music.get_busy():
            self.after_cancel(self.loopID)
            self.slider_val.set(value)
            self.Play()
        else:
            self.slider_val.set(value)

    def Stop(self):
        """Stop the playing of the track"""
        if self.player.music.get_busy():
            self.playBut.config(image=self.play, command=self.Play)
            update.set("Ready")
            l.update()
            self.player.music.stop()

    def Repeat(self):
        if self.player.music.get_busy():
            playtime = 0
            self.UpdateSlider(playtime)
            self.player.music.rewind()

    def Fast(self):
        playtime = self.slider_val.get()
        playtime += 5
        self.UpdateSlider(playtime)

    def Back(self):
        playtime = self.slider_val.get()
        playtime -= 5
        self.UpdateSlider(playtime)

    def Next(self):
        new = os.path.basename(text.get())
        dir1 = text.get().replace(f"/{new}", "")
        songs = os.listdir(dir1)
        i = j = 0
        while i < len(songs):
            if songs[i] == new:
                j = i
                j += 1
            i += 1
        path = dir1 + f"/{songs[j]}"
        sec_win(path)

    def Prev(self):
        new = os.path.basename(text.get())
        dir1 = text.get().replace(f"/{new}", "")
        songs = os.listdir(dir1)
        i = j = 0
        while i < len(songs):
            if songs[i] == new:
                j = i
                j -= 1
            i += 1
        path = dir1 + f"/{songs[j]}"
        sec_win(path)


def OpenFile():
    global file
    file = askopenfilename(defaultextension=".mp3", filetypes=[("All Files", "*"), ("Audio Files", "*.mp3")])
    if file == "":
        file = None
    else:
        path = os.path.dirname(file)
        f = os.path.basename(file)
        f = path + f"/{f}"
        text.set(f)
        entry1.update()


def New_Window():
    try:
        window = Toplevel()
        file = text.get()
        a = os.path.basename(file)
        window.title(a)
        app = MusicPlayer(window, file, tracktype='mp3')
        app.Play()
        app.grab_set()
        update.set("Playing...")
        l.update()
        window.mainloop()
    except Exception as e:
        print(e)
        tmsg.showinfo("Error", "Please enter the file name or provide a valid file")
        window.destroy()


def sec_win(path):
    win = Toplevel()
    file = path
    a = os.path.basename(file)
    win.title(a)
    app = MusicPlayer(win, file, tracktype='mp3')
    app.Play()
    app.grab_set()
    text.set(path)
    entry1.update()
    win.mainloop()


root = Tk()
root.title("Player")
root.geometry("400x200")
text = StringVar()
text.set("")
update = StringVar()
update.set("Ready")
Label(root, text="Select a file : ", font="Georgia 16").pack()
entry1 = Entry(root, textvariable=text, relief=RIDGE)
entry1.pack()
Button(root, text="Browse", bd=4, relief=RAISED, command=OpenFile, font="Butterfly 12").pack(pady=10)
Button(root, text="Play", bd=4, relief=RAISED, bg="green", command=New_Window, font="Butterfly 12", fg="white").pack(
    pady=10)
l = Label(root, textvar=update, relief=GROOVE, anchor="w", fg="green")
l.pack(side=BOTTOM, fill=X)
root.mainloop()
