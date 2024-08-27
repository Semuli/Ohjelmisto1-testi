vuosi = int(input("kerro vuosi:"))

if vuosi % 100 == 0 and vuosi % 400 != 0 :
    print("Ei karkaus vuos")
elif vuosi % 100 == 0 and vuosi % 400 == 0 :
    print("Karkausvuosi")
elif vuosi % 4 == 0 :
    print("karkausvuosi")
else:
    print("ei karkausvuosi!")