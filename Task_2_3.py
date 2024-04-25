print("Факториал числа ", end="")
n = int(input())
fa = 1
for i in range(1,n+1):
    fa = fa*i
print(f" равен {fa}")