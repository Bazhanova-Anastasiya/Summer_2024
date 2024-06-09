import re
s = "Например, LDDDLL78 или LDDDLL178, или A123BC78 или X666XX178 или А222ТЕ123 Е346ЕО178"
p = r"[ABCEKMHOPTXАВСЕКМНОРТХ]\d{3}[ABCEKMHOPTXАВСЕКМНОРТХ][ABCEKMHOPTXАВСЕКМНОРТХ][1]?[7][8]"
print(re.findall(p,s))