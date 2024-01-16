import sqlite3
connection = sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(user)
connection.close()
