from tkinter import *
import Number_Converter


def convert():
    f = from_base.get()
    t = to_base.get()
    # n = int(num.get())
    if f == "2-(Binary)" and t == "10-(Decimal)":
        n=num.get()
        n = Number_Converter.BinaryToDecimal(n)
        result_var.set(n)
        text2.update()
    elif f == "2-(Binary)" and t == "8-(Octal)":
        n=num.get()
        n = Number_Converter.BinaryToOctal(n)
        result_var.set(n)
        text2.update()
    elif f == "2-(Binary)" and t == "16-(Hexadecimal)":
        n=num.get()
        n = Number_Converter.BinaryToHexadecimal(n)
        result_var.set(n)
        text2.update()
    elif f == "8-(Octal)" and t == "2-(Binary)":
        n=(num.get())
        n = Number_Converter.OctalToBinary(n)
        result_var.set(n)
        text2.update()
    elif f == "8-(Octal)" and t == "10-(Decimal)":
        n=num.get()
        n = Number_Converter.OctalToDecimal(n)
        result_var.set(n)
        text2.update()
    elif f == "8-(Octal)" and t == "16-(Hexadecimal)":
        n=num.get()
        n = Number_Converter.OctalToHexadecimal(n)
        result_var.set(n)
        text2.update()
    elif f == "10-(Decimal)" and t == "2-(Binary)":
        n=(num.get())
        n = Number_Converter.DecimalToBinary(n)
        result_var.set(n)
        text2.update()
    elif f == "10-(Decimal)" and t == "8-(Octal)":
        n=num.get()
        n = Number_Converter.DecimalToOctal(n)
        result_var.set(n)
        text2.update()
    elif f == "10-(Decimal)" and t == "16-(Hexadecimal)":
        n=(num.get())
        n = Number_Converter.DecimalToHexadecimal(n)
        result_var.set(n)
        text2.update()
    elif f == "16-(Hexadecimal)" and t == "2-(Binary)":
        n=num.get()
        n = Number_Converter.HexadecimalToBinary(n)
        result_var.set(n)
        text2.update()
    elif f == "16-(Hexadecimal)" and t == "10-(Decimal)":
        n=num.get()
        n = Number_Converter.HexadecimalToDecimal(n)
        result_var.set(n)
        text2.update()


options = ["2-(Binary)", "8-(Octal)", "10-(Decimal)", "16-(Hexadecimal)"]

root = Tk()
root.geometry("400x400")
root.maxsize(400,400)
root.minsize(400,400)
root.title("Number System Converter")
root.config(bg="grey")

from_base = StringVar()
from_base.set("Base")
to_base = StringVar()
to_base.set("Base")
num = StringVar()
num.set("")
result_var = StringVar()
result_var.set("")

Label(root,text="Number System Converter",font="Algerian 16 underline",fg="white",bg="black").pack()
Label(root, text="Enter Number", font="Georgia 14",fg="white",bg="grey").pack(pady=15)

text1 = Entry(root, textvar=num)
text1.pack(pady=10)

Label(root, text="From", font="Georgia 14",fg="white",bg="grey").pack()

op1 = OptionMenu(root, from_base, *options)
op1.pack()

Label(root, text="To", font="Georgia 14",fg="white",bg="grey").pack()

op2 = OptionMenu(root, to_base, *options)
op2.pack()

Button(root, text="Convert", bg="gold", fg="black", bd=4, padx=16, relief=RAISED, command=convert,font="Arial 12 bold").pack(pady=25)

Label(root, text="Result", font="Georgia 14",fg="white",bg="grey").pack()

text2 = Entry(root, textvar=result_var)
text2.pack()

root.mainloop()
