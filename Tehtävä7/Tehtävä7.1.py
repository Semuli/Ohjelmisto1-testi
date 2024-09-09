def vuodenaika(numero):
    if 3<=numero<=5:
        return "kevättä"
    elif 6<=numero<=8:
        return "kesää"
    elif 9<=numero<=10:
        return "syksyä"
    else:
        return "talvea"

kuukaudet = ("Tammi", "Helmi", "Maalis", "Huhti", "Touko", "Kesä", "Heinä", "Elo", "Syys", "Loka", "Marras", "Joulu")

numero = int(input("Anna kuukausi:"))
kuukausi = kuukaudet[numero-1]

print(f"Kuukausi on {kuukausi}kuu, ja se on {vuodenaika(numero)}")

