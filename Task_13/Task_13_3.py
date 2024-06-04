lst = [1,2,3,4,5,6,7,8,9,10]
def nechet(lst):
    lst2 = []
    for i in lst:
        if i % 2 == 1: yield i
        lst2.append(i)
g = nechet(lst)
for k in g:
    print(k, end=" ")
