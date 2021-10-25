import cv2
from pyzbar import pyzbar
from tkinter import *
import tkinter.messagebox as tmsg


def recognize(frame):
    try:
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            with open("Result.txt", "w") as f:
                f.write(f"Result : {barcode_info}")

    except Exception as e:
        pass
    return frame


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


root = Tk()
root.config(bg="Black")
root.geometry("400x150")
root.title("QR Code and Barcode Reader")
Label(root, text="QR Code and Barcode Reader", fg="gold", font="Algerian 16", bg="black").pack()
Button(root, text="Start", relief=RAISED, bd=4, bg="green", fg="white", font="Georgia 18", command=main).pack(pady=5)
Label(root, text="*Press q to exit", fg="red", bg="black", font="Butterfly 14").pack(pady=5)
root.mainloop()
