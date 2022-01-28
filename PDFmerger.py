import img2pdf
from tkinter import *
from tkinter.filedialog import askopenfilename
import os


def OpenFile():
    global file
    file = askopenfilename(defaultextension=".png", filetypes=[("All Files", "*"), ("Image Files", "*.png")])
    if file == "":
        file = None
    else:
        path = os.path.dirname(file)
        f = os.path.basename(file)
        f = path + f"/{f}"
        file1.set(f)
        path2.update()


files = []


def addfile():
    files.append(file1.get())
    file1.set("")


def convert():
    up.set("Generating...")
    l.update()
    with open("name.pdf", "wb") as f:
        f.write(img2pdf.convert(files))
    up.set("Done")
    l.update()


root = Tk()
root.title("PDF Maker")
file1 = StringVar()
file1.set("")
up = StringVar()
up.set("Ready")
root.geometry("400x200")
heading = Label(root, text="PDF Maker", font=("Microsoft Sans Serif", 16))
heading.pack()
path2 = Entry(root, textvariable=file1, bd=4, relief=RAISED, width=60)
path2.pack(padx=15)
l = Label(root, textvariable=up, relief=GROOVE, anchor="sw", fg="green")
l.pack(side=BOTTOM, fill=X)
browse = Button(root, bg="green", text="Browse", relief=RAISED, command=OpenFile, font="Georgia 14 italic", fg="gold")
browse.pack(side=LEFT, padx=15, ipadx=15)
add = Button(root, bg="green", text="Add", relief=RAISED, command=addfile, font="Georgia 14 italic", fg="gold")
add.pack(side=LEFT, padx=15, ipadx=15)
start = Button(root, bg="green", text="Generate", relief=RAISED, command=convert, font="Georgia 14 italic", fg="gold")
start.pack(padx=15, ipadx=15, pady=41)
root.mainloop()
if __name__ == '__main__':
    print(file1)
    print(files)
