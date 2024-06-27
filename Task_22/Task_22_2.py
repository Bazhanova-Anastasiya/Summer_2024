import keyword
s = "You can dance, import you can jive, global def having the time of your life False as"
lst = s.split()
lst2 = []
print(lst)
for i in lst:
    if i in keyword.kwlist:
        lst2.append("<kw>")
    else:
        print(i)
        lst2.append(i)
print(" ".join(lst2))
