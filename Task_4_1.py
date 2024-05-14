s = input().split()
if s[1] == '+':
    print(float(s[0]) + float(s[2]))
elif s[1] == '-':
    print(float(s[0]) - float(s[2]))
elif s[1] == '*':
    print(float(s[0]) * float(s[2]))
elif s[1] == '/':
    if float(s[2]) == 0:
        print("Деление на ноль невозможно")
    else:
        print(float(s[0]) / float(s[2]))
else:
    print('Неверный знак операции!')



