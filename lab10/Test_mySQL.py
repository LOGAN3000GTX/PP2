import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aa@25032004",
    database="world"
)

CursorDB = mydb.cursor()

# CursorDB.execute("SELECT * FROM City LIMIT 10;")
# CursorDB.execute("SELECT Language FROM CountryLanguage WHERE CountryCode = 'RUS';")
# CursorDB.execute("SELECT * FROM City LIMIT 5 OFFSET 20;")
# CursorDB.execute("SELECT * FROM country WHERE NOT name = 'Germany' or not name = 'Spain'")
# CursorDB.execute("SELECT * FROM country ORDER BY name ASC") or you can add desc
# CursorDB.execute("SELECT city.  Name AS cities, country.Name AS countries FROM city JOIN country ON city.CountryCode = country.Code")
# CursorDB.execute("SELECT MAX(Population) AS MIN_POPULATION FROM city")
CursorDB.execute("SELECT country.Continent, city.Population, countrylanguage.Language, countrylanguage.Percentage FROM country CROSS JOIN city CROSS JOIN countrylanguage LIMIT 5")

for i in CursorDB:
    print(i)
CursorDB.close()

# My_cursor = mydb.cursor()
# My_cursor.execute("CREATE DATABASE my_database") This is how to create our database if you want
# My_cursor.execute("SHOW DATABASES") This command visualise how many databases we have
# My_cursor.execute("CREATE TABLE suppliers (name VARCHAR(255), address VARCHAR(255), phone VARCHAR(255));")
# My_cursor.execute("ALTER TABLE suppliers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;")
# My_cursor.execute("SELECT * FROM suppliers;")
# My_cursor.execute("SELECT Name FROM suppliers WHERE Name = 'Baltic Peat'")
# My_cursor.execute("SELECT address FROM suppliers WHERE address LIKE '%Pet%'")

"""
for result in My_cursor.fetchall():
    print(result)

My_cursor.close()
"""

"""
sql = "INSERT INTO suppliers (name, address, phone) VALUES (%s, %s)"
val = [("Fabrica Torfa", "Ekaterenburg Sverdlov region Belinskogo 222", "+77772134571"),
       ("Baltic Peat", "Sanct-Peterburg", "+77235467328"),
       ("Irkutsk kora", "Irkutsk", "+77017808912")
       ]

My_cursor.executemany(sql, val)

mydb.commit()

print(My_cursor.rowcount, "Record inserted.")
"""


