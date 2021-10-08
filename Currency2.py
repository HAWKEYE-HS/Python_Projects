from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
currencies = ["AED", "AFN", "ALN", "AMD", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD",
              "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP",
              "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK",
              "DOP", "DZD", "EGP", "ERN", "ETB", "EUR",
              "FKP", "GBP", "GEL", "GHS", "GIP", "GMD",
              "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS",
              "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KPW", "KRW", "KWD",
              "KYD", "KZT", "LAK", "LBP", 'LKR', "LRD", "LSL", "LYD",
              "MAD", "MDL", "MGA"",MKD", "MMK", "MNT", "MOP", "MRU", "MUR",
              "MVR", "MWK", "USD"]


def Bit():
    def convert():
        import requests
        import json
        try:
            form = "BTC"
            to = clicked1.get()
            link = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=4KADD7Z6B5RZOTJH" % (
                form, to)
            r = requests.get(link).text
            rate_dict = json.loads(r)
            dict1 = rate_dict["Realtime Currency Exchange Rate"]
            conv_fact = float(dict1["5. Exchange Rate"])
            amt1 = amt.get()
            converted = amt1 * conv_fact
            val.set(converted)
            Text2.update()
        except Exception as e:
            showinfo("Error","Check your Internet Connection")
            bit_window.destroy()
    bit_window = Toplevel()
    bit_window.geometry("550x350")
    bit_window.grab_set()
    bit_window.title("BITCOIN CONVERTER")
    amt = IntVar()
    amt.set("")
    val = IntVar()
    val.set("")
    clicked1 = StringVar()
    clicked1.set("Select Currency")
    Label(bit_window, text="BitCoin Converter", font="Georgia 20 underline").pack()
    Text1 = Entry(bit_window, textvar=amt, font="Lucida 14")
    Text1.pack(pady=25)
    Label(bit_window,text="BTC",bd=2,relief=SUNKEN,font="Lucida 14").pack()
    Text2 = Entry(bit_window, textvar=val, font="Lucida 14")
    Text2.pack(pady=25)
    drop = OptionMenu(bit_window, clicked1, *currencies)
    drop.pack(pady=25)
    f = Frame(bit_window)
    Button(f, text="Convert", font=("Microsoft Sans Serif", 16, "bold"), bd=4, bg="gold", fg="black",
           activebackground="red",command=convert).pack()
    f.pack()


def Curr():
    def convert():
        import requests
        import json
        try:
            form = clicked1.get()
            to = clicked2.get()
            link = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=4KADD7Z6B5RZOTJH" % (
                form, to)
            r = requests.get(link).text
            rate_dict = json.loads(r)
            dict1 = rate_dict["Realtime Currency Exchange Rate"]
            conv_fact = float(dict1["5. Exchange Rate"])
            amt1 = amt.get()
            converted = amt1 * conv_fact
            val.set(converted)
            Text2.update()
        except Exception as e:
            showinfo("Error","Check your Internet Connection")
            curr_window.destroy()
    curr_window = Toplevel()
    curr_window.geometry("550x450")
    curr_window.title("CURRENCY CONVERTER")
    amt = IntVar()
    amt.set("")
    val = IntVar()
    val.set("")
    clicked1 = StringVar()
    clicked1.set("Select Currency")
    clicked2 = StringVar()
    clicked2.set("Select Currency")
    Label(curr_window, text="Currency Converter", font="Georgia 20 underline").pack()
    Text1 = Entry(curr_window, textvar=amt, font="Lucida 14")
    Text1.pack(pady=25)
    drop = OptionMenu(curr_window, clicked1, *currencies)
    drop.pack(pady=25)
    Text2 = Entry(curr_window, textvar=val, font="Lucida 14")
    Text2.pack(pady=25)
    drop = OptionMenu(curr_window, clicked2, *currencies)
    drop.pack(pady=25)
    f = Frame(curr_window)
    Button(f, text="Convert", font=("Microsoft Sans Serif", 16, "bold"), bd=4, bg="green", fg="white",
           activebackground="red", command=convert).pack()
    f.pack()
    curr_window.grab_set()


if __name__ == '__main__':
    root = Tk()
    root.title("Currency")
    root.geometry("550x500")
    root.config(bg="black")
    Label(root, text="Converter", font="Algerian 20 bold",bg="black",fg="white").pack()
    img = Image.open("Currency_logo.JPG")
    img = img.resize((215, 234), Image.ANTIALIAS)
    curr = ImageTk.PhotoImage(img)
    img1 = Image.open("Bitcoin.png")
    img1 = img1.resize((215, 234), Image.ANTIALIAS)
    BTC = ImageTk.PhotoImage(img1)
    Button(root, image=BTC, text="Bitcoin Converter", compound=TOP, command=Bit,font="Georgia 14",bg="black",fg="white",relief=RIDGE,bd=2).pack(padx=25, side=LEFT)
    Button(root, image=curr, text="Currency Converter", compound=TOP, command=Curr,font="Georgia 14",bg="black",fg="white",relief=RIDGE,bd=2).pack(padx=25, side=LEFT)
    root.mainloop()
