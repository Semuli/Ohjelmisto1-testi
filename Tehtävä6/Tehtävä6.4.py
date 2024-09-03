def tulo(lista):
    luku = 0
    for i in lista:
        luku += int(i)
    return luku

lista = []
numero = 0

while numero != "":
    numero = input("anna numero: ")
    if numero.isnumeric():
        lista.append(numero)

print(lista)

tulos = tulo(lista)
print(tulos)