lst = [10,3,7,9,15]
minch = lst[0]
for x in lst:
    if lst[1] < minch: minch = lst[1]
    if lst[2] < minch: minch = lst[2]
    if lst[3] < minch: minch = lst[3]
    if lst[4] < minch: minch = lst[4]
print("Наименьшее число из списка lst", minch)
