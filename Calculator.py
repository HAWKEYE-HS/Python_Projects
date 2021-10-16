from tkinter import *


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
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()


nums = ['7', '8', '9', "*", "4", "5", "6", "-", "1", "2", "3", "+", "%", "0", "C", "="]
root = Tk()
root.geometry("500x600")
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
    if i==15:
        b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="orange", fg="white")
        b.pack(side=LEFT, padx=7, pady=7)
        b.bind("<Button-1>", click)
    elif i==14:
        b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="orange")
        b.pack(side=LEFT, padx=7, pady=7)
        b.bind("<Button-1>", click)
    else:
        b = Button(f, text=nums[i], font="Lucida 35 bold", padx=10, bg="black", fg="white")
        b.pack(side=LEFT, padx=7, pady=7)
        b.bind("<Button-1>", click)
f.pack()
root.mainloop()
