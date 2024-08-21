print("Anna keskiaisten mittojen määrät")
Leiviskä = input("leiviskä: ")
Naula = input("Naula: ")
Luoti = input("Luoti: ")

Luoti_paino = 13.3
Naula_paino = (Luoti_paino) * 32
Leiviskä_paino = (Naula_paino) * 20

Massa = (Leiviskä_paino * float(Leiviskä)) + (Naula_paino * float(Naula)) + (Luoti_paino * float(Luoti))
Massa_kilot = int(Massa/1000)
Massa_grammat = Massa - (Massa_kilot * 1000)

print(f"{Massa_kilot:2.0f} kilogrammaa ja {Massa_grammat:<.2f} grammaa."  )