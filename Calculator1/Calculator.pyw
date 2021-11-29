from tkinter import *

import Inverse_2x2
import Inverse_3x3
import Inverse_4x4
import lin2
import lin
import Determinant_2x2, Determinant_3x3, Determinant_4x4
import Transpose


def factorial():
    n = int(sc_value.get())
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    sc_value.set(fact)
    screen.update()


def lin_equ_win():
    win = Toplevel()
    win.geometry("300x150")
    win.title("Linear Equations")
    Label(win, text="Number of Unknowns ? ", font="Butterfly 16  underline", fg="blue").pack()
    Button(win, text="2", font="Georgia 14", fg="gold", bg="black", padx=15, command=lin.main).pack(pady=14)
    Button(win, text="3", font="Georgia 14", fg="gold", bg="black", padx=15, command=lin2.main).pack()
    win.grab_set()


def deter1():
    win = Toplevel()
    win.geometry("300x220")
    win.title("Determinant")
    Button(win, text="2x2", font="Georgia 14", fg="gold", bg="black", padx=15, command=Determinant_2x2.main).pack(
        pady=14)
    Button(win, text="3x3", font="Georgia 14", fg="gold", bg="black", padx=15, command=Determinant_3x3.main).pack(
        pady=14)
    Button(win, text="4x4", font="Georgia 14", fg="gold", bg="black", padx=15, command=Determinant_4x4.main).pack(
        pady=14)
    win.grab_set()


def deter2():
    win = Toplevel()
    win.geometry("300x220")
    win.title("Inverse")
    Button(win, text="2x2", font="Georgia 14", fg="gold", bg="black", padx=15, command=Inverse_2x2.main).pack(
        pady=14)
    Button(win, text="3x3", font="Georgia 14", fg="gold", bg="black", padx=15, command=Inverse_3x3.main).pack(
        pady=14)
    Button(win, text="4x4", font="Georgia 14", fg="gold", bg="black", padx=15, command=Inverse_4x4.main).pack(
        pady=14)
    win.grab_set()


def matrix():
    win = Toplevel()
    win.geometry("300x300")
    win.title("Matrix")
    Label(win, text="Operations : ", font="Butterfly 16  underline", fg="blue").pack()
    Button(win, text="Determinant", font="Georgia 14", fg="gold", bg="black", padx=15, command=deter1).pack(pady=14)
    Button(win, text="Inverse", font="Georgia 14", fg="gold", bg="black", padx=15, command=deter2).pack(pady=14)
    Button(win, text="Transpose", font="Georgia 14", fg="gold", bg="black", padx=15, command=Transpose.ask).pack(pady=14)
    win.grab_set()


def click(event):
    global sc_value
    text = event.widget.cget("text")
    if text == "=":
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        else:
            try:
                value = eval(sc_value.get())
            except Exception as e:
                value = "Error"
        sc_value.set(value)
        screen.update()
    elif text == "C":
        sc_value.set("")
        screen.update()
    elif text == "LinEqu":
        sc_value.set("")
        screen.update()
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()


nums = ['7', '8', '9', "*", "4", "5", "6", "-", "1", "2", "3", "+", "/", "0", "C", "=", "LinEqu", "!", "Mat"]
root = Tk()
root.geometry("500x700")
root.configure(bg="black")
root.title("Calculator")
sc_value = StringVar()
sc_value.set("")
screen = Entry(root, textvar=sc_value, font="Georgia 40 bold", bg="black", fg="white")
screen.pack(ipadx=8, fill=X, padx=10, pady=10)
f = Frame(root, bg="black")
for i in range(0, 4):
    b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="white")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg="black")
for i in range(4, 8):
    b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="white")
    b.pack(side=LEFT, padx=11, pady=11)
    b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg="black")
for i in range(8, 12):
    b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="white")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()
f = Frame(root, bg="black")
for i in range(12, 16):
    if i == 15:
        b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="orange", fg="white")
        b.pack(side=LEFT, padx=7, pady=7)
        b.bind("<Button-1>", click)
    elif i == 14:
        b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="orange")
        b.pack(side=LEFT, padx=7, pady=7)
        b.bind("<Button-1>", click)
    else:
        b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="white")
        b.pack(side=LEFT, padx=7, pady=7)
        b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="black")
for i in range(16, 19):
    if i == 16:
        b = Button(f, text=nums[i], font="Lucida 24 bold", padx=10, bg="black", fg="white", command=lin_equ_win)
        b.pack(side=LEFT, padx=10, pady=10)
        b.bind("<Button-1>", click)
    elif i == 17:
        b = Button(f, text=nums[i], font="Lucida 24 bold", padx=10, bg="black", fg="white", command=factorial)
        b.pack(side=LEFT, padx=10, pady=10)
    elif i == 18:
        b = Button(f, text=nums[i], font="Lucida 24 bold", padx=10, bg="black", fg="white", command=matrix)
        b.pack(side=LEFT, padx=10, pady=10)
f.pack()
root.mainloop()
