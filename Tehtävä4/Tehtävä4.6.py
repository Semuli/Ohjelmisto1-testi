import random
import math

arvotaan = int(input("montako kertaa arvotaan:"))
arvottu = int(0)

sisalla = int(0)
ulkona = int(0)

while arvottu < arvotaan:
    x = random.randint(-10000000, 10000000) / 10000000
    y = random.randint(-10000000, 10000000) / 10000000
    #print(x, y)
    if (x ** 2) + (y ** 2) < 1 :
        sisalla = sisalla + 1
    else :
        ulkona = ulkona + 1
    arvottu = arvottu + 1
    #print(arvottu)

#print(sisalla, ulkona, arvottu)
likiarvo = (4 * int(sisalla)) / int(arvottu)

print("likiarvo", likiarvo)
print(math.pi)