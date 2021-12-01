from scipy import linalg
from tkinter import *
import numpy as np

numsl = []
cont = []
A = B = C = D = []
question = []
MA = MB = MC = MD = ""


class main:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Matrix")
        self.root.geometry("400x370")
        nums = ['7', '8', '9', "4", "5", "6", "1", "2", "3", "0", "-", "+", "C", "=", "|__|", "MatA", "MatB", "MatC",
                "MatD"]
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
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.add_Mat)
                b.pack(side=LEFT, padx=7, pady=7)
                # b.bind("<Button-1>", self.click)
            else:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white")
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
        f.pack()
        f = Frame(self.root, bg="black")
        for i in range(15, 19):
            if i == 15:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white", command=MatrixA)
                b.pack(side=LEFT, padx=7, pady=7)
            elif i == 16:
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="white", command=MatrixB)
                b.pack(side=LEFT, padx=7, pady=7)
            # b.bind("<Button-1>", self.click)
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
            question.append(self.sc_value.get().split(" + ")[0])
            self.sc_value.set("")
            self.screen.update()
            print(question)

    def add_Mat(self):

        # print(question[0])
        if question[0] == 'MatA' and question[1] == 'MatB':
            x = MA + MB
            print(x)


class mainA:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Determinant 3X3")
        self.root.geometry("400x370")
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
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.defA)
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
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
                numsl.append(self.sc_value.get())
                self.sc_value.set("")
                self.screen.update()
            if text != "|__|":
                self.sc_value.set(self.sc_value.get() + text)
                self.screen.update()
        print(numsl)
        if len(numsl) == 13:
            self.defA()

    def defA(self):
        self.sc_value.set("")
        self.screen.update()
        m = int(cont[0])
        n = int(cont[1])
        MatA = np.zeros((m, n))
        k = 0
        while k < len(numsl):
            for i in range(m):
                for j in range(n):
                    MatA[i][j] = numsl[k]
                    k += 1
        print(MatA)
        MA = MatA.copy()
        numsl.clear()
        self.root.destroy()
        cont.clear()


class MatrixA:
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
        app2 = mainA()


class mainB:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Determinant 3X3")
        self.root.geometry("400x370")
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
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange", command=self.defB)
                b.pack(side=LEFT, padx=7, pady=7)
                b.bind("<Button-1>", self.click)
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
                numsl.append(self.sc_value.get())
                self.sc_value.set("")
                self.screen.update()
            if text != "|__|":
                self.sc_value.set(self.sc_value.get() + text)
                self.screen.update()
        print(numsl)
        if len(numsl) == 13:
            self.defB()

    def defB(self):
        self.sc_value.set("")
        self.screen.update()
        m = int(cont[0])
        n = int(cont[1])
        MatB = np.zeros((m, n))
        k = 0
        while k < len(numsl):
            for i in range(m):
                for j in range(n):
                    MatB[i][j] = numsl[k]
                    k += 1
        print(MatB)
        MB = MatB.copy()
        numsl.clear()
        cont.clear()
        self.root.destroy()


class MatrixB:
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
        app2 = mainB()


if __name__ == '__main__':
    app = main()
