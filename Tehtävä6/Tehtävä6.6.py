import math

def pizza_hinta(halkaisia_cm, hinta):
    halkaisia_m = halkaisia_cm / 100
    pinta_ala = math.pi * ((halkaisia_m / 2 ) ** 2)
    hinta_m = hinta / pinta_ala
    return hinta_m

pizza1_hinta = float(input("Ensimmäisen pizzan hinta €: "))
pizza1_halkaisia = float(input("Ensimmäisen pizzan halkasia CM: "))

pizza2_hinta = float(input("Toisen pizzan hinta €: "))
pizza2_halkaisia = float(input("Toisen pizzan halkasia CM: "))

pizza1_hinta_m = pizza_hinta(pizza1_halkaisia, pizza1_hinta)
pizza2_hinta_m = pizza_hinta(pizza2_halkaisia, pizza2_hinta)

print(f"ensimmäisen pizza {pizza1_hinta_m:.2f} €/m^2")
print(f"toisen pizza {pizza2_hinta_m:.2f} €/m^2")

if pizza1_hinta_m > pizza2_hinta_m:
    print("Toisen pizzan neliö hinta on parempi")
elif pizza1_hinta_m < pizza2_hinta_m:
    print("Ensimmäisen pizzan  neliö hinta on parempi")
elif pizza1_hinta_m == pizza2_hinta_m:
    print("Samam arvoiset")