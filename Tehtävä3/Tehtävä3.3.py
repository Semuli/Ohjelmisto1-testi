Sukupuoli = input("Kerro sukupuolesi:")
Hemoglobiini = input("ja hemoglobiini arvo (g/l):")

if Sukupuoli.upper() == "MIES" and Hemoglobiini < str(134):
    print("Hemoglobiini arvosi ovat liian alhaiset")
elif Sukupuoli.upper() == "MIES" and Hemoglobiini > str(195):
    print("Hemoglobiini arvosi ovat liian korkeat")
elif Sukupuoli.upper() == "MIES":
    print("Hemoglobiini arvosi ovat sopivat")
elif Sukupuoli.upper() == "NAINEN" and Hemoglobiini < str(117):
    print("Hemoglobiini arvosi ovat liian alhaiset")
elif Sukupuoli.upper() == "NAINEN" and Hemoglobiini > str(175):
    print("Hemoglobiini arvosi ovat liian korkeat")
elif Sukupuoli.upper() == "NAINEN":
    print("Hemoglobiini arvosi ovat sopivat")
else:
    print("Vastausta ei löydy")