import numpy as np
from tkinter import *

numsl = []

cont = []


class main:
    def __init__(self):
        self.root = Toplevel()
        self.root.config(bg="black")
        self.root.title("Transpose")
        self.root.geometry("300x300")
        nums = ['7', '8', '9', "4", "5", "6", "1", "2", "3", "0", "-", "+", "C", "=", "|__|", "-->"]
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
        for i in range(12, 16):
            if i == 14:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="orange", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            elif i == 13:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.tra)
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            elif i == 15:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.tra)
                b.pack(side=LEFT, padx=7, pady=7)
                # b.bind("<Button-1>", self.click)
            else:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
        f.pack()
        self.root.grab_set()

    def click(self, event):
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

    def tra(self):
        self.sc_value.set("")
        self.screen.update()
        m = int(cont[0])
        n = int(cont[1])
        B = np.zeros((m, n))
        k = 0
        while k < len(numsl):
            for i in range(m):
                for j in range(n):
                    B[i][j] = numsl[k]
                    k += 1
        x = B.transpose()
        win = Toplevel()
        win.title("Answer")
        win.geometry("300x200")
        que = f"{str(B)}"
        ans = f"{str(x)}"
        Label(win, text="Original Matrix : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=que, font="Georgia 12", fg="green").pack()
        Label(win, text="Transpose : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=ans, font="Georgia 12", fg="green").pack()
        print(f'Determinant of \n{B} \n is {x}')
        numsl.clear()
        win.grab_set()
        self.root.destroy()


class ask:
    def __init__(self):
        self.window = Toplevel()
        self.window.title("")
        self.window.config(bg="black")
        self.window.geometry("300x300")
        nums = ['7', '8', '9', "4", "5", "6", "1", "2", "3", "0", "-", "+", "C", "=", "|__|", "-->"]
        self.sc_value = StringVar()
        self.sc_value.set("Rows ? ")
        self.screen = Entry(self.window, textvar=self.sc_value, font="Georgia 20 bold", bg="black", fg="white")
        self.screen.pack(ipadx=8, fill=X, padx=10, pady=10)
        f = Frame(self.window, bg="black")
        for i in range(0, 4):
            b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.window, bg="black")
        for i in range(4, 8):
            b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
            b.pack(side=LEFT, padx=11, pady=11)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.window, bg="black")
        for i in range(8, 12):
            b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
            b.pack(side=LEFT, padx=10, pady=10)
            b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.window, bg="black")
        for i in range(12, 16):
            if i == 14:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="orange", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            elif i == 13:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            elif i == 15:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.next)
                b.pack(side=LEFT, padx=7, pady=7)
                # b.bind("<Button-1>", self.click)
            else:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
        f.pack()
        self.window.grab_set()

    def click(self, event):
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
                cont.append(self.sc_value.get().split(" ? ")[1])
                self.sc_value.set("Columns ? ")
                self.screen.update()
            if text != "|__|":
                self.sc_value.set(self.sc_value.get() + text)
                self.screen.update()
        print(cont)

    def next(self):
        self.window.destroy()
        app2 = main()


if __name__ == '__main__':
    app = ask()
