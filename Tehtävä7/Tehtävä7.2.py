nimet = set()

while True:
    uusi_nimi = input("Anna uusi nimi tai paina entter:")
    if uusi_nimi == '':
        break
    elif uusi_nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(uusi_nimi)
        print("Uusi nimi")

print(nimet)