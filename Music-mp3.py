from tkinter import *
from mutagen.mp3 import MP3
from mutagen import MutagenError
from pygame import mixer
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame


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
        f = Frame(self)
        self.playBut = Button(f, image=self.play, command=self.Play)
        self.playBut.pack(side=LEFT, padx=20, pady=10)

        self.stopBut = Button(f, image=self.pause, command=self.Stop)
        self.stopBut.pack(side=LEFT, padx=20, pady=10)

        self.stopBut = Button(f, image=self.repeat, command=self.Repeat)
        self.stopBut.pack(side=LEFT, padx=20, pady=10)
        f.pack()
        self.slider_val = DoubleVar()
        self.slider = Scale(self, to=self.tracklength, orient=HORIZONTAL, length=700, resolution=0.5, showvalue=True,
                            tickinterval=30, digit=4, variable=self.slider_val, command=self.UpdateSlider)
        self.slider.pack(side=RIGHT)

    def Play(self):
        """Play track from slider location"""
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
            self.player.music.stop()

    def Repeat(self):
        if self.player.music.get_busy():
            playtime = 0
            self.UpdateSlider(playtime)
            self.player.music.rewind()


def New_Window(file, image):
    window = Toplevel()
    a = file.split("\\")[5]
    img = Image.open(image)
    img = img.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    window.title(a)
    Label(window, image=photo).pack()
    app = MusicPlayer(window, file, tracktype='mp3')
    app.grab_set()
    window.mainloop()


def play1():
    New_Window('C:\\Users\\colorado.colorado-PC\\Desktop\\Music123\\Alone.mp3', "Alone.jpeg")


def play2():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Believer.mp3', "Believer.jpeg")


def play3():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Blinding lights.mp3', "Blinding Lights.jpeg")


def play4():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Capital Letters.mp3', "Capital Letters.jpeg")


def play5():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Colour.mp3', "2")


def play6():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Despacito.mp3', "Despacito .jpeg")


def play7():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Echame la Clupa.mp3', "Echame LA Clupa.jpeg")


def play8():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Eenie Menie.mp3', "Eenie Meenie.jpeg")


def play9():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Faded.mp3', "Faded.jpeg")


def play10():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Happy (from Despicable Me 2) G I R L - 320Kbps.mp3',
               "Happy.jpeg")


def play11():
    New_Window(r'C:\Users\colorado.colorado-PC\Desktop\Music123\Peaches.mp3', "Peaches.jpeg")


if __name__ == '__main__':
    root = Tk()
    root.title("Music")
    root.geometry("500x500")
    f1 = Frame(root, bg="grey")
    f1.pack(fill=X)
    l1 = Label(f1, fg="purple", text="Music Player", font=("Algerian", 24, "bold"), bd=5, relief=RAISED)
    l1.pack()
    f2 = Frame(root)
    f2.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f2, text="(1) Alone", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play1)
    b1.pack(side=LEFT)
    f3 = Frame(root)
    f3.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f3, text="(2) Believer", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play2)
    b1.pack(side=LEFT)
    f4 = Frame(root)
    f4.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f4, text="(3) Blinding Lights", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play3)
    b1.pack(side=LEFT)
    f5 = Frame(root)
    f5.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f5, text="(4) Capital Letters", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play4)
    b1.pack(side=LEFT)
    f6 = Frame(root)
    f6.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f6, text="(5) Colour", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play5)
    b1.pack(side=LEFT)
    f7 = Frame(root)
    f7.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f7, text="(5) Despacito", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play6)
    b1.pack(side=LEFT)
    f8 = Frame(root)
    f8.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f8, text="(6) Echame la Clupa", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play7)
    b1.pack(side=LEFT)
    f9 = Frame(root)
    f9.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f9, text="(7) Eenie Menie", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play8)
    b1.pack(side=LEFT)
    f10 = Frame(root)
    f10.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f10, text="(8) Faded", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play9)
    b1.pack(side=LEFT)
    f11 = Frame(root)
    f11.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f11, text="(9) Happy", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play10)
    b1.pack(side=LEFT)
    f12 = Frame(root)
    f12.pack(side=TOP, anchor="nw", pady=5, padx=10)
    b1 = Button(f12, text="(10) Peaches", bg="white", fg="green", font=("Georgia", 12, "italic"),
                relief=SUNKEN, command=play11)
    b1.pack(side=LEFT)
    root.mainloop()
