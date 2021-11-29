from scipy import linalg
import numpy as np
from tkinter import *

numsl = []


class main:
    def __init__(self):
        self.root = Toplevel()
        self.root.config(bg="black")
        self.root.title("Determinant 4X4")
        self.root.geometry("300x300")
        nums = ['7', '8', '9', "4", "5", "6", "1", "2", "3", "0", "-", "+", "C", "=", "|__|"]
        self.sc_value = StringVar()
        self.sc_value.set("")
        self.screen = Entry(self.root, textvar=self.sc_value, font="Georgia 20 bold", bg="black", fg="white")
        self.screen.pack(ipadx=8, fill=X, padx=10, pady=10)
        f = Frame(self.root, bg="black")
        for i in range(0, 4):
            b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.root, bg="black")
        for i in range(4, 8):
            b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
            b.pack(side=LEFT, padx=11, pady=11)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.root, bg="black")
        for i in range(8, 12):
            b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.root, bg="black")
        for i in range(12, 15):
            if i == 14:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="orange", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            elif i == 13:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.solve_4x4)
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            else:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
        f.pack()
        self.root.grab_set()

    def click(self, event):
        # global sc_value
        text = event.widget.cget("text")
        if text == "=":
            if self.sc_value.get().isdigit():
                value = int(self.sc_value.get())
            else:
                try:
                    value = eval(self.sc_value.get())
                except Exception as e:
                    value = "Error"
            self.sc_value.set(value)
            self.screen.update()
        elif text == "C":
            self.sc_value.set("")
            self.screen.update()
        else:
            if text == "|__|":
                numsl.append(self.sc_value.get())
                self.sc_value.set("")
                self.screen.update()
            if text != "|__|":
                self.sc_value.set(self.sc_value.get() + text)
                self.screen.update()
        print(numsl)
        if len(numsl) ==16:
            self.solve_4x4()

    def solve_4x4(self):
        self.sc_value.set("")
        self.screen.update()
        A = np.array([[numsl[0], numsl[1], numsl[2], numsl[3]], [numsl[4], numsl[5], numsl[6], numsl[7]],
                      [numsl[8], numsl[9], numsl[10], numsl[11]], [numsl[12], numsl[13], numsl[14], numsl[15]]])
        x = linalg.det(A)
        win = Toplevel()
        win.title("Answer")
        win.geometry("300x200")
        que = f"{str(A)}"
        ans = f"{str(x)}"
        Label(win, text="Input : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=que, font="Georgia 12", fg="green").pack()
        Label(win, text="Output : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=ans, font="Georgia 12", fg="green").pack()
        print(f'Determinant of \n{A} \n is {x}')
        numsl.clear()
        win.grab_set()


if __name__ == '__main__':
    app = main()
