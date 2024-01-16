import sqlite3
connection = sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('''
SELECT usernsame, age
FROM Users
WHERE age=(SELECT MAX(age)FROM Users)
''')
oldest_users=cursor.fetchall()
for user in oldest_users:
    print(user)
connection.close()