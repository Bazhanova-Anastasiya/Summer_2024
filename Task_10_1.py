f_1 = open('test1.txt', "r", encoding='utf-8')
lst = f_1.readlines()
f_1.close()
print(lst)

f_2 = open('test2.txt', 'w', encoding='utf-8')
for i in lst[::-1]:
    print(' '.join(i.split()[::-1]), file = f_2)
f_2.close()

f_1 = open('test2.txt', 'r', encoding='utf-8')
lst = f_1.readlines()
f_1.close()
print(lst)
