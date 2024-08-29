import random

noppia = input("Montako noppaa: ")

summa = 0

if noppia != "":
    for heittoa in range(int(noppia)):
        summa = summa + random.randint(1,6)
        print(summa)

print(f"Summa lopulta {summa}")