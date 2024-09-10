import mysql.connector

def get_airport_type_amount(iso_country):
    sql = f'SELECT type, count(*) FROM airport WHERE iso_country = "{iso_country}" GROUP BY type'
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

iso_country = input("Kerro maatunnus:")

tyyppi_maarat = get_airport_type_amount(iso_country)

for tyyppi in tyyppi_maarat:
    print(f"Tyyppi:{tyyppi['type']} määrä:{tyyppi['count(*)']}")
