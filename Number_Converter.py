hexnum = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
decnum = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}


# TESTED
def BinaryToDecimal(n):
    if '.' in n:
        n1 = int(n.split(".")[0])
        n2 = n.split(".")[1]
        l = len(n2)
        n2 = int(n2)
        ans1 = ans2 = 0
        x1 = x2 = 1
        i = 1
        while n1 > 0:
            y1 = int(n1 % 10)
            ans1 += x1 * y1
            x1 *= 2
            n1 /= 10
        while i <= l:
            i += 1
        i -= 1
        while n2 > 0:
            y2 = int(n2 % 10)
            x2 = pow(2, -i)
            ans2 += x2 * y2
            i -= 1
            n2 /= 10
        ans = ans1 + ans2
        return ans
    else:
        n = int(n)
        ans = 0
        x = 1
        while n > 0:
            y = int(n % 10)
            ans += x * y
            x *= 2
            n /= 10
        return ans


# TESTED
def BinaryToOctal(n):
    dec = str(BinaryToDecimal(n))
    oct = DecimalToOctal(dec)
    return oct


# TESTED
def BinaryToHexadecimal(n):
    dec = str(BinaryToDecimal(n))
    hexa = DecimalToHexadecimal(dec)
    return hexa


# TESTED
def OctalToBinary(n):
    ans = ""
    if "." in n:
        n1 = int(n.split(".")[0])
        n2 = int(n.split(".")[1])
        ans1 = ""
        ans2 = ""
        while n1 > 0:
            q = int(n1 % 10)
            if q == 0:
                ans1 = "".join(["000 ", ans1])
            elif q == 1:
                ans1 = "".join(["001 ", ans1])
            elif q == 2:
                ans1 = "".join(["010 ", ans1])
            elif q == 3:
                ans1 = "".join(["011 ", ans1])
            elif q == 4:
                ans1 = "".join(["100 ", ans1])
            elif q == 5:
                ans1 = "".join(["101 ", ans1])
            elif q == 6:
                ans1 = "".join(["110 ", ans1])
            elif q == 7:
                ans1 = "".join(["111 ", ans1])
            else:
                break
            n1 = int(n1 / 10)
        while n2 > 0:
            q = int(n2 % 10)
            if q == 0:
                ans2 = "".join(["000 ", ans2])
            elif q == 1:
                ans2 = "".join(["001 ", ans2])
            elif q == 2:
                ans2 = "".join(["010 ", ans2])
            elif q == 3:
                ans2 = "".join(["011 ", ans2])
            elif q == 4:
                ans2 = "".join(["100 ", ans2])
            elif q == 5:
                ans2 = "".join(["101 ", ans2])
            elif q == 6:
                ans2 = "".join(["110 ", ans2])
            elif q == 7:
                ans2 = "".join(["111 ", ans2])
            else:
                break
            n2 = int(n2 / 10)
        ans = ans1 + "." + ans2
    else:
        n = int(n)
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


# TESTED
def OctalToDecimal(n):
    if '.' in n:
        n1 = int(n.split(".")[0])
        n2 = n.split(".")[1]
        l = len(n2)
        n2 = int(n2)
        ans1 = ans2 = 0
        x1 = x2 = 1
        i = 1
        while n1 > 0:
            y1 = int(n1 % 10)
            ans1 += x1 * y1
            x1 *= 8
            n1 /= 10
        while i <= l:
            i += 1
        i -= 1
        while n2 > 0:
            y2 = int(n2 % 10)
            x2 = pow(8, -i)
            ans2 += x2 * y2
            i -= 1
            n2 /= 10
        ans = ans1 + ans2
        return ans
    else:
        n = int(n)
        ans = 0
        x = 1
        while n > 0:
            y = int(n % 10)
            ans += x * y
            x *= 8
            n /= 10
        return ans


# TESTED
def OctalToHexadecimal(n):
    dec = str(OctalToDecimal(n))
    hexa = DecimalToHexadecimal(dec)
    return hexa


# TESTED
def DecimalToOctal(n):
    if "." in n:
        num1 = int(n.split(".")[0])
        n = float(n)
        num = n * pow(8, 5)
        ans = ""
        while num > 0:
            rem = int(num % 8)
            if num == num1:
                ans = "".join([f"{str(rem)}.", ans])
            else:
                ans = "".join([str(rem), ans])
            num = int(num / 8)
        return ans
    else:
        n = int(n)
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


# TESTED
def DecimalToBinary(n):
    if "." in n:
        num1 = int(n.split(".")[0])
        n = float(n)
        num = n * pow(2, 5)
        ans = ""
        while num > 0:
            rem = int(num % 2)
            if num == num1:
                ans = "".join([f"{str(rem)}.", ans])
            else:
                ans = "".join([str(rem), ans])
            num = int(num / 2)
        return ans
    else:
        n = int(n)
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


# TESTED
def DecimalToHexadecimal(n):
    if "." in n:
        num1 = int(n.split(".")[0])
        n = float(n)
        num = n * pow(16, 5)
        ans = ""
        while num > 0:
            r = int(num % 16)
            if num == num1:
                if r == 10 or r == 11 or r == 12 or r == 13 or r == 14 or r == 15:
                    ans = "".join([f"{str(r)}.", ans])
                    ans = ans.replace(str(r), hexnum[str(r)])
                else:
                    ans = "".join([f"{str(r)}.", ans])
            else:
                if r == 10 or r == 11 or r == 12 or r == 13 or r == 14 or r == 15:
                    ans = "".join([str(r), ans])
                    ans = ans.replace(str(r), hexnum[str(r)])
                else:
                    ans = "".join([str(r), ans])
            num = int(num / 16)
        return ans
    else:
        ans = ""
        n = int(n)
        while n > 0:
            r = int(n % 16)
            if r == 10 or r == 11 or r == 12 or r == 13 or r == 14 or r == 15:
                ans = "".join([hexnum[str(r)], ans])
            else:
                ans = "".join([str(r), ans])
            n = int(n / 16)
        return ans


# def HexadecimalToDecimal(n):
#     ans = ""
#     x = 1
#     s = len(n)
#     i = s - 1
#     while i >= 0:
#         if '0' <= n[i] <= '9':
#             ans += x * int((n[i] - '0'))
#         elif 'A' <= n[i] <= 'F':
#             ans += x * int((n[i] - 'A' + 10))
#         x *= 16
#         i = i - 1
#     return ans
def HexadecimalToDecimal(n):
    if '.' in n:
        n1 = int(n.split(".")[0])
        n2 = n.split(".")[1]
        l = len(n2)
        n2 = int(n2)
        ans1 = ans2 = 0
        x1 = x2 = 1
        i = 1
        while n1 > 0:
            y1 = int(n1 % 10)
            ans1 += x1 * y1
            x1 *= 16
            n1 /= 10
        while i <= l:
            i += 1
        i -= 1
        while n2 > 0:
            y2 = int(n2 % 10)
            x2 = pow(16, -i)
            ans2 += x2 * y2
            i -= 1
            n2 /= 10
        ans = ans1 + ans2
        return ans
    else:
        n2 = []
        a = 0
        # print(type(n1))
        j = 0
        while j < len(n):
            j += 1
        print(f"Initial : {j}")
        for i in n:
            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
                n2.append(i.replace(i, decnum[i]))
                n = n.replace(i, "")
        # print(n2[1])
        while len(n2) > 0:
            ans1 = n2[a] * pow(16, j)
            j -= 1
            a += 1
            print(f"n2:{n2[a]}")
            print(f"j:{j}")
            print(f"a:{a}")
        n = int(n)
        ans = 0
        x = 1
        while n > 0:
            y = int(n % 10)
            ans += x * y
            x *= 16
            n /= 10
        return ans + ans1


# TESTED
def HexadecimalToBinary(n):
    ans = ""
    if "." in n:
        n2 = ""
        ans1 = ""
        ans2 = ""
        j = len(n) - 1
        while j >= 0:
            n2 += n[j]
            j -= 1
        n1 = n2.split(".")[0]
        n3 = n2.split(".")[1]
        for i in n1:
            if i == "0":
                ans1 = "".join(["0000 ", ans1])
            elif i == '1':
                ans1 = "".join(["0001 ", ans1])
            elif i == "2":
                ans1 = "".join(["0010 ", ans1])
            elif i == "3":
                ans1 = "".join(["0011 ", ans1])
            elif i == "4":
                ans1 = "".join(["0100 ", ans1])
            elif i == "5":
                ans1 = "".join(["0101 ", ans1])
            elif i == "6":
                ans1 = "".join(["0110 ", ans1])
            elif i == "7":
                ans1 = "".join(["0111 ", ans1])
            elif i == "8":
                ans1 = "".join(["1000 ", ans1])
            elif i == "9":
                ans1 = "".join(["1001 ", ans1])
            elif i == "A":
                ans1 = "".join(["1010 ", ans1])
            elif i == "B":
                ans1 = "".join(["1011 ", ans1])
            elif i == "C":
                ans1 = "".join(["1100 ", ans1])
            elif i == "D":
                ans1 = "".join(["1101 ", ans1])
            elif i == "E":
                ans1 = "".join(["1110 ", ans1])
            elif i == "F":
                ans1 = "".join(["1111 ", ans1])
            else:
                break
        for i in n3:
            if i == "0":
                ans2 = "".join(["0000 ", ans2])
            elif i == '1':
                ans2 = "".join(["0001 ", ans2])
            elif i == "2":
                ans2 = "".join(["0010 ", ans2])
            elif i == "3":
                ans2 = "".join(["0011 ", ans2])
            elif i == "4":
                ans2 = "".join(["0100 ", ans2])
            elif i == "5":
                ans2 = "".join(["0101 ", ans2])
            elif i == "6":
                ans2 = "".join(["0110 ", ans2])
            elif i == "7":
                ans2 = "".join(["0111 ", ans2])
            elif i == "8":
                ans2 = "".join(["1000 ", ans2])
            elif i == "9":
                ans2 = "".join(["1001 ", ans2])
            elif i == "A":
                ans2 = "".join(["1010 ", ans2])
            elif i == "B":
                ans2 = "".join(["1011 ", ans2])
            elif i == "C":
                ans2 = "".join(["1100 ", ans2])
            elif i == "D":
                ans2 = "".join(["1101 ", ans2])
            elif i == "E":
                ans2 = "".join(["1110 ", ans2])
            elif i == "F":
                ans2 = "".join(["1111 ", ans2])
            else:
                break
        ans = ans2 + "." + ans1
        return ans
    else:
        n2 = ""
        j = len(n) - 1
        while j >= 0:
            n2 += n[j]
            j -= 1
        for i in n2:
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


# def HexadecimalToOctal(n):
#     bin = str(HexadecimalToDecimal(n))
#     octa = BinaryToOctal(bin)
#     return octa


if __name__ == '__main__':
    num = input("Enter a hex number : ")
    print(HexadecimalToDecimal(num))
