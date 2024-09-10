import mysql.connector

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport Where ident = "{icao}"'
    cursor = connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

connection = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database= 'flight_game',
    user= 'root',
    password= 'Kissa123',
    autocommit=True
    )

icao = input("kerro icao:")

airport = get_airport_by_icao(icao)
print(airport)