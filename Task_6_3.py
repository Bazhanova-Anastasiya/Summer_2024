import string
s = input()
lett = {}
num = {}
for i in s:
    if i not in string.ascii_letters: print(i, end=' ')
    elif i in "0123456789": print(i, end=' ')
    else: print(i, end=' ')