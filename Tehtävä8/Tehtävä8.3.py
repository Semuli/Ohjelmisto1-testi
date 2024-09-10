import mysql.connector
from geopy import distance

def get_airport_cordinates(icao):
    sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
    cursor = connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

def get_airport_name_by_icao(icao):
    sql = f'SELECT name FROM airport Where ident = "{icao}"'
    cursor = connection.cursor()
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

airport1 = input("Kerro ensimmäisen kentän ICAO-koodi:")
airport2 = input("Kerro toisen kentän ICAO-koodi:")

airport1_location = get_airport_cordinates(airport1)
airport1_name = get_airport_name_by_icao(airport1)
airport2_location = get_airport_cordinates(airport2)
airport2_name = get_airport_name_by_icao(airport2)
dist = distance.distance(airport1_location, airport2_location)

print(f"Kenttien {airport1_name[0][0]} ja {airport2_name[0][0]} etäisyys toisistaan on: {dist}")