from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import os


def NewFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-NotePad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def SaveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-NotePad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def Cut():
    TextArea.event_generate("<<Cut>>")


def Copy():
    TextArea.event_generate("<<Copy>>")


def Paste():
    TextArea.event_generate("<<Paste>>")


def About():
    showinfo("Help", "Notepad by Hawkeye")


root = Tk()
root.geometry("1000x1000")
root.title("Untitled-NotePad")
TextArea = Text(root, font="Georgia 14")
file = None
TextArea.pack(fill=BOTH, expand=True)
MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=NewFile)
FileMenu.add_command(label="Open", command=OpenFile)
FileMenu.add_command(label="Save", command=SaveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quit)
MenuBar.add_cascade(label="File", menu=FileMenu)

EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label="Cut", command=Cut)
EditMenu.add_command(label="Copy", command=Copy)
EditMenu.add_command(label="Paste", command=Paste)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About", command=About)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
root.config(menu=MenuBar)
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
root.mainloop()
