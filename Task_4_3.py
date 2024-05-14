s1 = input()
s2 = input()
dct1 = {}
for i in s1:
    if i not in dct1:
        dct1[i] = 1
    else: dct1[i] += 1
dct2 = {}
for i in s2:
    if i not in dct2:
        dct2[i] = 1
    else: dct2[i] += 1
print(dct1)
print(dct2)
print(dct1 == dct2)


