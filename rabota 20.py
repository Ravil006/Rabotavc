import sqlite3
connection = sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unknown_age_users=cursor.fetchall()
for user in unknown_age_users:
    print(user)
connection.close()