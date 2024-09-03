import random

def noppa(sivua):
    luku = random.randint(1, int(sivua))
    return luku

luku = 0
heittoja = 0

tahkoa = int(input("moniko sivuista noppaa heitetään: "))


while luku != tahkoa:
    luku = noppa(tahkoa)
    print(luku)
    heittoja += 1

print(f"heittoja yhteensä: {heittoja}")