import mysql.connector

conn = mysql.connector.connect(
    host="localhost",       
    user="root",            
    password="password",    
    database="your_database" 
)

cursor = conn.cursor()

data = [
    ("Fluffy", "Harold", "chat", "f", "2013--02-04", None),
    ("Claws", "Gwen", "chat", "m", "2014-03-17", None),
    ("Buffy", "Harod", "chien", "f", "2019-0513", None),
    ("Fang", "Benny", "chien", "m", "2010-08-27", None),
    ("Bowser", "Diane", "chien", "m", "2018-08-31", "2021-07-29"),
    ("Chirpy", "Gwen", "oiseau", "f", "2018-09-11", None),
    ("Whistler", "Gwen", "oiseau", None, "2017-12-09", None),
    ("Slim", "Benny", "serpent", "m", "2016-04-29", None),
    ("Puffball", "Diane", "hamster", "f", "2019-03-30", None)
]

insert_query = """
INSERT INTO animals (name, owner, species, gender, birth, death)
VALUES (%s, %s, %s, %s, %s, %s)
"""

try:
    cursor.executemany(insert_query, data)
    conn.commit()
    print(f"{cursor.rowcount} enregistrements ont été insérés.")
except mysql.connector.Error as err:
    print(f"Erreur: {err}")
finally:
    cursor.close()
    conn.close()
