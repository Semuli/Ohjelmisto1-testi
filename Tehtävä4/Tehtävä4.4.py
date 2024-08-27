import random

luku = random.randint(1, 10)

arvaus = input("arvaa numero:")


while luku != int(arvaus) :
    if float(luku) < float(arvaus) :
       print("pienempi")
    elif float(luku) > float(arvaus) :
        print("suurempi")
    arvaus = input("arvaa:")

print("OIKEIN!")