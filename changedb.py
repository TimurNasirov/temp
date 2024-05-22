from sqlite3 import connect

connect = connect('database.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute('ALTER TABLE messages ADD COLUMN reply INTEGER)')
