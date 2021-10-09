def BinaryToDecimal(n):
    ans = 0
    x = 1
    while n > 0:
        y = int(n % 10)
        ans += x * y
        x *= 2
        n /= 10
    return ans


def BinaryToOctal(n):
    dec = BinaryToDecimal(n)
    oct = DecimalToOctal(dec)
    return oct


def BinaryToHexadecimal(n):
    dec = BinaryToDecimal(n)
    hexa = DecimalToHexadecimal(dec)
    return hexa


def OctalToBinary(n):
    ans = ""
    while n > 0:
        q = int(n % 10)
        if q == 0:
            ans = "".join(["000 ", ans])
        elif q == 1:
            ans = "".join(["001 ", ans])
        elif q == 2:
            ans = "".join(["010 ", ans])
        elif q == 3:
            ans = "".join(["011 ", ans])
        elif q == 4:
            ans = "".join(["100 ", ans])
        elif q == 5:
            ans = "".join(["101 ", ans])
        elif q == 6:
            ans = "".join(["110 ", ans])
        elif q == 7:
            ans = "".join(["111 ", ans])
        else:
            break
        n = int(n / 10)
    return ans


def OctalToDecimal(n):
    ans = 0
    x = 1
    while n > 0:
        y = int(n % 10)
        ans += x * y
        x *= 8
        n /= 10
    return ans


def OctalToHexadecimal(n):
    dec = OctalToDecimal(n)
    hexa = DecimalToHexadecimal(dec)
    return hexa


def DecimalToOctal(n):
    ans = 0
    x = 1
    while x <= n:
        x *= 8
    x /= 8
    while n > 0:
        lastDigit = int(n / x)
        n -= lastDigit * x
        x /= 8
        ans = ans * 10 + lastDigit
    return ans


def DecimalToBinary(n):
    ans = 0
    x = 1
    while x <= n:
        x *= 2
    x /= 2
    while n > 0:
        lastDigit = int(n / x)
        n -= lastDigit * x
        x /= 2
        ans = ans * 10 + lastDigit
    return ans


def HexadecimalToDecimal(n):
    ans = ""
    x = 1
    s = len(n)
    i = s - 1
    while i >= 0:
        if '0' <= n[i] <= '9':
            ans += x * int((n[i] - '0'))
        elif 'A' <= n[i] <= 'F':
            ans += x * int((n[i] - 'A' + 10))
        x *= 16
        i = i - 1
    return ans


def DecimalToHexadecimal(n):
    return hex(n).replace("0x", " ").upper()


def HexadecimalToBinary(n):
    ans = ""
    l = len(n)
    for i in n:
        if i == "0":
            ans = "".join(["0000 ", ans])
        elif i == '1':
            ans = "".join(["0001 ", ans])
        elif i == "2":
            ans = "".join(["0010 ", ans])
        elif i == "3":
            ans = "".join(["0011 ", ans])
        elif i == "4":
            ans = "".join(["0100 ", ans])
        elif i == "5":
            ans = "".join(["0101 ", ans])
        elif i == "6":
            ans = "".join(["0110 ", ans])
        elif i == "7":
            ans = "".join(["0111 ", ans])
        elif i == "8":
            ans = "".join(["1000 ", ans])
        elif i == "9":
            ans = "".join(["1001 ", ans])
        elif i == "A":
            ans = "".join(["1010 ", ans])
        elif i == "B":
            ans = "".join(["1011 ", ans])
        elif i == "C":
            ans = "".join(["1100 ", ans])
        elif i == "D":
            ans = "".join(["1101 ", ans])
        elif i == "E":
            ans = "".join(["1110 ", ans])
        elif i == "F":
            ans = "".join(["1111 ", ans])
        else:
            break
    return ans


if __name__ == '__main__':
    num = int(input("Enter a octal number : "))
    print(OctalToHexadecimal(num))
