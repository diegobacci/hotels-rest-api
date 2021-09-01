import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hoteis (id_hotel TEXT PRIMARY KEY, nome TEXT,\
                estrela REAL, valor_diaria REAL, cidade TEXT)"

create_hotel = "INSERT INTO hoteis VALUES ('omega', 'Omega Hotel', 4.6, 1219, 'Indaiatuba')"

cursor.execute(create_table)
cursor.execute(create_hotel)

connection.commit()  # Envia o statement para o banco
connection.close()