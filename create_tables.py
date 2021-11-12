import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table_1 = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY , name text, price real)"
cursor.execute(create_table_1)

# insert_table = "INSERT INTO items VALUES (1, 'Redmi 5', 25000.00)"
# cursor.execute(insert_table)

connection.commit()
connection.close()