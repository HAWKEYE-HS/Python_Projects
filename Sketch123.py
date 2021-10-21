import cv2
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import tkinter.messagebox as tmsg


def convert():
    try:
        img = text.get()
        path = text.get().replace(os.path.basename(text.get()), "")
        f2 = os.path.basename(text.get()).split(".")[0]
        f3 = f"{f2}-2.jpg"
        f4 = os.path.join(path, f3)
        image = cv2.imread(img)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted_image = 255 - gray_image
        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        cv2.imshow("Original Image", image)
        cv2.imshow("Pencil Sketch", pencil_sketch)
        cv2.imwrite(f4, pencil_sketch)
        cv2.waitKey(0)
    except Exception as e:
        print(e)
        tmsg.showinfo("Error", "Select a file or provide a valid file")


def OpenFile():
    global file
    file = askopenfilename(defaultextension=".jpg", filetypes=[("All Files", "*"), ("Image Files", "*.jpg")])
    if file == "":
        file = None
    else:
        path = os.path.dirname(file)
        f = os.path.basename(file)
        f = path + f"/{f}"
        text.set(f)
        entry1.update()


root = Tk()
root.config(bg="gray")
root.geometry("300x200")
root.title("Sketch Maker")
text = StringVar()
text.set("")
Label(root, text="Select a file : ", font="Georgia 16", fg="gold", bg="gray").pack()
entry1 = Entry(root, textvariable=text, relief=RIDGE)
entry1.pack(expand=True)
Button(root, text="Browse", bd=4, relief=RAISED, command=OpenFile, font="Butterfly 12", bg="red", fg="white").pack(
    pady=10)
Button(root, text="Convert", bd=4, relief=RAISED, bg="green", font="Butterfly 12", fg="white", command=convert).pack(
    pady=10)
root.mainloop()
