import numpy
import pandas as pd
dct = {"Товар": ["Масло", "Молоко", "Творог", "Сметана", "Йогурт"],
           "Шт": [5, 7, 20, 15, 5],
           "Цена": [90, 70, 60, 80, 30]}
df = pd.DataFrame(dct)
print(df)
print("________________________")
su = 0
for i in df.index:
    for j in df.columns:
        x = df.loc[i, j]
        if type(x) == numpy.int64:
            su = su + x
print(su)

