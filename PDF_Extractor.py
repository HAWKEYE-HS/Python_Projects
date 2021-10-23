from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import tkinter.messagebox as tmsg


def convert():
    import PyPDF2
    n = filename.get()
    num = number.get()
    f = PyPDF2.PdfFileReader(text.get())
    o = f.getPage(num).extractText()
    update.set("Extracting...")
    l.update()
    with open(n, "w") as f:
        for i in o:
            f.write(i)
    update.set("Done")
    l.update()
    tmsg.showinfo("Success",f"Extracted successfully. Check {n} file to see the extracted text")


def OpenFile():
    global file
    file = askopenfilename(defaultextension=".pdf", filetypes=[("All Files", "*"), ("Text Documents", "*.pdf")])
    if file == "":
        file = None
    else:
        path = os.path.dirname(file)
        f = os.path.basename(file)
        f = path + f"/{f}"
        text.set(f)
        entry1.update()


root = Tk()
root.title("PDF Extractor")
root.geometry("400x300")
text = StringVar()
text.set("")
filename = StringVar()
number = IntVar()
number.set("")
update = StringVar()
update.set("Ready")
Label(root, text="Select a file : ", font="Georgia 12").pack()
entry1 = Entry(root, textvariable=text)
entry1.pack(expand=True)
Button(root, text="Browse", bd=4, relief=RAISED, command=OpenFile, font="Butterfly 12").pack(pady=10,
                                                                                             padx=87)
Label(root, text="Provide the name of destination file : ", font="Georgia 12").pack()
entry2 = Entry(root, textvariable=filename)
entry2.pack(expand=True)
Label(root, text="Provide a page number : ", font="Georgia 12").pack()
entry3 = Entry(root, textvariable=number)
entry3.pack(expand=True)
Button(root, text="Extract", bd=4, relief=RAISED, bg="green", font="Butterfly 12", fg="white", command=convert).pack(
    pady=10)
l = Label(root, textvar=update, relief=GROOVE, anchor="w")
l.pack(side=BOTTOM, anchor="n", fill=X)
root.mainloop()
