def litroiksi(gallonaa):
    litraa = 3.785 * gallonaa
    return litraa

gallonaa = float(input("anna gallona määrä: "))

while gallonaa >= 0:
    litraa = litroiksi(gallonaa)
    print(f"{litraa: .3f} litraa")
    gallonaa = float(input("seuraava gallona määrä: "))