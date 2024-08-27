luku1 = float(input("kerro luku:"))

pienin = suurin = luku = luku1

while luku != "":
    if float(luku) > float(suurin) :
        suurin = luku
    if float(luku) < float(pienin) :
        pienin = luku
    luku = input("kerro luku:")
else:
    print(f"suurin arvo oli {suurin}")
    print(f"pienin arvo oli {pienin}")