summa=0
k=0
while True:
    i = float(input())
    if i == 0:
        break
    summa = summa + i #сумма всех зарплат
    k = k + 1 #кол-во сотрудников
print("Средняя зарплата", summa/k)