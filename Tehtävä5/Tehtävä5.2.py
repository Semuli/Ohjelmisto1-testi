lista = []

luku = input("kerro luku:")

while luku != "":
    lista.append(luku)
    luku = input("kerro toinen luku:")

lista.sort(reverse=True)

print(lista[0:5])