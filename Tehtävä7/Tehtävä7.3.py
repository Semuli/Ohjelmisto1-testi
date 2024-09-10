lentoasemat = {"EFAA":"Aavahelukka Airport","EFHK":"Helsinki Vantaa Airport"}

vastaus = input("Kerro haluatko: \n1 Syöttää uuden lentoaseman \n2 hakea jo syötetyn lentoaseman tiedot \n3 lopettaa \n:")

while vastaus != "3":
    if vastaus == "1":
        icao = input("Anna lentoaseman ICAO-koodi:")
        nimi = input("Ja anna lentoaseman nimi:")
        lentoasemat[icao] = nimi
    elif vastaus == "2":
        haku = input("Anna lentoaseman ICAO-koodi:")
        if haku in lentoasemat:
            print(f"{haku} ICAO-Koodi on {lentoasemat[haku]}")
    vastaus = input("Kerro haluatko: \n1 Syöttää uuden lentoaseman \n2 hakea jo syötetyn lentoaseman tiedot \n3 lopettaa \n:")
else:
    print("suoritus päättyy")