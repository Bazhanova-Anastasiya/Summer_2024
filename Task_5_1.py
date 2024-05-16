n = int(input())
lst={}
for i in range(0, n):
    j=[1]
    for k in range(1, i):
        j.append(int(lst[i-1][k-1])+int(lst[i-1][k]))
    if i>0:
        j+=[1]
    lst[i]=j
for k,v in lst.items():
    print(v)