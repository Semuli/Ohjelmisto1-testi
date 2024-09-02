import math

luku = int(input("kerro kokonaisluku:"))

alkuluku = 0
i = 2

while i < math.sqrt(luku):
    if luku % i == 0:
        alkuluku += 1
    i += 1

if alkuluku != 0:
    print("ei alkuluku")
else:
    print("alkuluku")