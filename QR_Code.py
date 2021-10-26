import cv2
from pyzbar import pyzbar
from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import askopenfilename
import pyqrcode


def recognize(frame):
    try:
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            with open("Result.txt", "w") as f:
                f.write(barcode_info)

    except Exception as e:
        pass
    return frame


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


def main():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    while ret:
        ret, frame = cam.read()
        frame = recognize(frame)
        cv2.imshow("Barcode and QR Code Reader", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    tmsg.showinfo("Success", "Check 'Results.txt' file to see scanned content")
    cam.release()
    cv2.destroyAllWindows()


def image_recognize():
    img = cv2.imread(text.get())
    img = recognize(img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    tmsg.showinfo("Done", "Check 'Results.txt' file to see scanned content")


def generate_code():
    content = text2.get()
    url = pyqrcode.QRCode(content)
    url.png("QR_Code.png", 30)
    img = cv2.imread("QR_Code.png")
    cv2.imshow("QR Code", img)
    cv2.waitKey(0)
    tmsg.showinfo("Done", "Check 'QR_Code.png' file to get your QR Code")


root = Tk()
root.config(bg="gray")
root.geometry("460x650")
root.title("QR Code and Barcode Reader")
text = StringVar()
text.set("")
text2 = StringVar()
text2.set("")

Label(root, text="QR Code and Barcode Reader/Generator", fg="gold", font="Algerian 16 underline", bg="gray").pack()
canvas1 = Canvas(root)
canvas1.pack()
canvas1.config(bg="gray")
Label(canvas1, text="QR Code/Barcode Reader", font="Butterfly 14", bg="gray", fg="white").pack()
Button(canvas1, text="Start Camera", relief=RAISED, bd=4, bg="green", fg="white", font="Georgia 18", command=main).pack(pady=5)
Label(canvas1, text="*Press q to exit", fg="red", bg="gray", font="Butterfly 14").pack(pady=5)
Label(canvas1, text="OR", font="Georgia 24 bold", bg="gray", fg="gold").pack()
# canvas2=Canvas(root)
# canvas2.pack()
# canvas2.config(bg="gray")
Label(canvas1, text="Upload a file", font="Butterfly 14", bg="gray", fg="white").pack()
entry1 = Entry(canvas1, textvariable=text, width=40)
entry1.pack()
Button(canvas1, text="Browse", font="Calibri 14", bg="green", fg="white", command=OpenFile).pack(pady=15)
Button(canvas1, text="Start", font="Calibri 14", bg="green", fg="white", command=image_recognize).pack(pady=15)
Label(root, text="______________________________________________", font="Georgia 24 bold", bg="gray", fg="white").pack(pady=15)
canvas3 = Canvas(root)
canvas3.pack()
canvas3.config(bg="gray")
Label(canvas3, text="Generate QR Code", font="Butterfly 14", bg="gray", fg="white").pack()
entry2 = Entry(canvas3, textvariable=text2, width=40)
entry2.pack()
Button(canvas3, text="Generate", font="Calibri 14", bg="green", fg="white", command=generate_code).pack(pady=15)
root.mainloop()
