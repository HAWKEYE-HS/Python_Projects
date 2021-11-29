import numpy as np
from tkinter import *

# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.array([[7, 8, 9], [10, 11, 12]])
# x = A + B
# print(x)

MatA = MatB = MatC = MatD = []


class main:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Inverse 3X3")
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
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.inv_3x3)
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
            elif i == 15:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
            else:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
        f.pack()
        self.root.mainloop()

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
                MatA.append(self.sc_value.get())
                self.sc_value.set("")
                self.screen.update()
            if text != "|__|":
                self.sc_value.set(self.sc_value.get() + text)
                self.screen.update()
        print(MatA)
        # if len(MatA) == 13:
        #     self.inv_3x3()

    def inv_3x3(self):
        self.sc_value.set("")
        self.screen.update()
        A = np.array([[MatA[0], MatA[1], MatA[2]], [MatA[3], MatA[4], MatA[5]], [MatA[6], MatA[7], MatA[8]]])
        B = np.array([[MatB[0], MatB[1], MatB[2]], [MatB[3], MatB[4], MatB[5]], [MatB[6], MatB[7], MatB[8]]])
        x = A + B
        win = Toplevel()
        win.title("Answer")
        win.geometry("300x200")
        que1 = f"{str(A)}"
        que2 = f"{str(B)}"
        ans = f"{str(x)}"
        Label(win, text=" Matrix A : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=que1, font="Georgia 12", fg="green").pack()
        Label(win, text=" Matrix B : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=que2, font="Georgia 12", fg="green").pack()
        Label(win, text=" Answer : ", font="Butterfly 16 italic", fg="blue").pack()
        Label(win, text=ans, font="Georgia 12", fg="green").pack()
        print(f'Determinant of \n{A} \n is {x}')
        MatA.clear()
        MatB.clear()
        win.grab_set()


if __name__ == '__main__':
    app = main()
