def parilliset(lista):
    lista2 = []
    for i in lista:
        if int(i) % 2 == 0:
            lista2.append(i)
    return lista2

numero = 0
lista = []

while numero != "":
    numero = input("anna numero: ")
    if numero.isnumeric():
        lista.append(numero)

lista2 = parilliset(lista)

print(f"lista: {lista}")
print(f"joista parillisai: {lista2}")