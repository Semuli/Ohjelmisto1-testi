import mysql.connector

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport Where ident = "{icao}"'
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

connection = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database= 'flight_game',
    user= 'mikko',
    password= 'salasana',
    autocommit=True
    )

icao = input("kerro icao:")

airport = get_airport_by_icao(icao)

for i in airport:
    print(f"Kentän nimi: {i['name']} ja sijainti kunta: {i['municipality']}")

if airport == []:
        print("Väärä ICAO_koodi")