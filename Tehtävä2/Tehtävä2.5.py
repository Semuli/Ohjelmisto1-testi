print("Anna keskiaisten mittojen määrät")
Leiviskä = input("leiviskä: ")
Naula = input("Naula: ")
Luoti = input("Luoti: ")

Leiviskä_paino = float(Leiviskä) * 20
Naula_paino = (Leiviskä_paino + float(Naula)) * 32
Luoti_paino = (Naula_paino + float(Luoti)) * 13.3

Massa = (Leiviskä_paino + Naula_paino + Luoti_paino)
Massa_kilot = int(Massa/1000)
Massa_grammat = Massa - (Massa_kilot * 1000)

print(Massa_grammat)
print(f"{Massa_kilot:2.0f}")
print("massa grammoina:" + str(Massa))

print(f"{Massa_kilot:2.0f} kilogrammaa ja {Massa_grammat:<.2f} grammaa."  )