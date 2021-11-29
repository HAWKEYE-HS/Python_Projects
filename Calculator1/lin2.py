from tkinter import *
from scipy import linalg
import numpy as np

numsl = []


class main:
    def __init__(self):
        self.root = Toplevel()
        self.root.config(bg="black")
        self.root.title("Simultaneous equation")
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
                b = Button(f, text=nums[i], font="Lucida 16 bold", bg="black", fg="orange",command=self.solve)
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
        if len(numsl) == 13:
            self.solve()

    def solve(self):
        x1 = numsl[0]
        y1 = numsl[1]
        z1 = numsl[2]
        x2 = numsl[4]
        y2 = numsl[5]
        z2 = numsl[6]
        x3 = numsl[8]
        y3 = numsl[9]
        z3 = numsl[10]
        c1 = numsl[3]
        c2 = numsl[7]
        c3 = numsl[11]
        try:
            a = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
            b = np.array([[c1], [c2], [c3]])
            ans = linalg.solve(a, b)
            win = Toplevel()
            win.title("Answer")
            win.geometry("300x200")
            a = f"{x1}x + {y1}y + {z1}z = {c1}\n" \
                f"{x2}x + {y2}y + {z2}z = {c2}\n" \
                f"{x3}x + {y3}y + {z3}z = {c3}\n"
            x = ans[0]
            y = ans[1]
            z = ans[2]
            Label(win, text=f"{a}", font="Georgia 12 italic", fg="blue").pack()
            Label(win, text="Answer : ", font="Georgia 12 italic", fg="red").pack()
            Label(win, text=f"x : {x}", font="Georgia 12 italic", fg="green").pack()
            Label(win, text=f"y : {y}", font="Georgia 12 italic", fg="green").pack()
            Label(win, text=f"z : {z}", font="Georgia 12 italic", fg="green").pack()
            print(f"Ans : {ans}")
        except Exception as e:
            print(e)
        numsl.clear()


if __name__ == '__main__':
    app = main()
