from tkinter import *
import Number_Converter


class main:
    def __init__(self):
        options = ["2-(Binary)", "8-(Octal)", "10-(Decimal)", "16-(Hexadecimal)"]

        self.root = Toplevel()
        self.root.geometry("400x400")
        self.root.maxsize(400, 400)
        self.root.minsize(400, 400)
        self.root.title("Number System Converter")
        self.root.config(bg="grey")

        self.from_base = StringVar()
        self.from_base.set("Base")
        self.to_base = StringVar()
        self.to_base.set("Base")
        self.num = StringVar()
        self.num.set("")
        self.result_var = StringVar()
        self.result_var.set("")

        Label(self.root, text="Number System Converter", font="Algerian 16 underline", fg="white", bg="black").pack()
        Label(self.root, text="Enter Number", font="Georgia 14", fg="white", bg="grey").pack(pady=15)

        text1 = Entry(self.root, textvar=self.num)
        text1.pack(pady=10)

        Label(self.root, text="From", font="Georgia 14", fg="white", bg="grey").pack()

        op1 = OptionMenu(self.root, self.from_base, *options)
        op1.pack()

        Label(self.root, text="To", font="Georgia 14", fg="white", bg="grey").pack()

        op2 = OptionMenu(self.root, self.to_base, *options)
        op2.pack()

        Button(self.root, text="Convert", bg="gold", fg="black", bd=4, padx=16, relief=RAISED, command=self.convert,
               font="Arial 12 bold").pack(pady=25)

        Label(self.root, text="Result", font="Georgia 14", fg="white", bg="grey").pack()

        self.text2 = Entry(self.root, textvar=self.result_var)
        self.text2.pack()

        self.root.grab_set()

    def convert(self):
        f = self.from_base.get()
        t = self.to_base.get()
        # n = int(num.get())
        if f == "2-(Binary)" and t == "10-(Decimal)":
            n = self.num.get()
            n = Number_Converter.BinaryToDecimal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "2-(Binary)" and t == "8-(Octal)":
            n = self.num.get()
            n = Number_Converter.BinaryToOctal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "2-(Binary)" and t == "16-(Hexadecimal)":
            n = self.num.get()
            n = Number_Converter.BinaryToHexadecimal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "8-(Octal)" and t == "2-(Binary)":
            n = (self.num.get())
            n = Number_Converter.OctalToBinary(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "8-(Octal)" and t == "10-(Decimal)":
            n = self.num.get()
            n = Number_Converter.OctalToDecimal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "8-(Octal)" and t == "16-(Hexadecimal)":
            n = self.num.get()
            n = Number_Converter.OctalToHexadecimal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "10-(Decimal)" and t == "2-(Binary)":
            n = (self.num.get())
            n = Number_Converter.DecimalToBinary(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "10-(Decimal)" and t == "8-(Octal)":
            n = self.num.get()
            n = Number_Converter.DecimalToOctal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "10-(Decimal)" and t == "16-(Hexadecimal)":
            n = (self.num.get())
            n = Number_Converter.DecimalToHexadecimal(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "16-(Hexadecimal)" and t == "2-(Binary)":
            n = self.num.get()
            n = Number_Converter.HexadecimalToBinary(n)
            self.result_var.set(n)
            self.text2.update()
        elif f == "16-(Hexadecimal)" and t == "10-(Decimal)":
            n = self.num.get()
            n = Number_Converter.HexadecimalToDecimal(n)
            self.result_var.set(n)
            self.text2.update()


if __name__ == '__main__':
    app = main()
