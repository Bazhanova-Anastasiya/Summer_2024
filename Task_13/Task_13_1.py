n= int(input())
def posledovatelnost(n):
    for i in range(1, n):
        if i % 2 == 1: yield i
        else: yield -i
g = posledovatelnost(n)
for k in g:
    print(k, end=" ")
