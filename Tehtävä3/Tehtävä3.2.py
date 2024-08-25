Hytti = input("kerro mikä hytti luokka (LUX, A, B, C):")
if Hytti.upper() == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif Hytti.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif Hytti.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif Hytti.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")