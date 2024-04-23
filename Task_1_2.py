x=float(input())
y=float(input())
a=x+y
b=x-y
c=x*y
d=x/y
e=x//y
if a>b and a>c and a>d and a>e:
    print(f"Наибольшее число {x+y=}")
elif b > a and b > c and b > d and b > e:
    print(f"Наибольшее число {x-y=}")
elif c > a and c > b and c > d and c > e:
    print(f"Наибольшее число {x*y=}")
elif d > a and d > b and d > c and d > e:
    print(f"Наибольшее число {x/y=}")
elif e > a and e > b and e > c and e > d:
    print(f"Наибольшее число {x//y=}")