lst = []
s = input()
n = int(input())
def code(string, n):
    for i in s:
        if 97 <= ord(i) < 122 or 65 <= ord(i) < 90:
            y = chr(ord(i) + n)
            lst.append(y)
        elif ord(i) == 122:
            y = chr(ord(i) - 25 + (n - 1))
            lst.append(y)
        elif ord(i) == 90:
            y = chr(ord(i) - 25 + (n - 1))
            lst.append(y)
        elif i.isdigit():
            lst.append(i)
        else:
            lst.append(i)
    return lst
a = code(s, n)
print(''.join(lst))

