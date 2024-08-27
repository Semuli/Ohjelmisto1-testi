käyttäjä_oikea = "python"
salasana_oikea = "rules"

käyttäjä = str(input("Anna käyttäjä:"))
salasana = str(input("Anna salasana:"))
yritys = int(0)

while käyttäjä != käyttäjä_oikea or salasana != salasana_oikea :
    yritys = int(yritys) + 1
    if int(yritys) >= 5 :
        print("Pääsy evätty")
        break
    käyttäjä = input("Anna käyttäjä uudestaa:")
    salasana = input("Anna salasana uudestaan:")


if käyttäjä == käyttäjä_oikea and salasana == salasana_oikea:
    print("Tervetuloa")