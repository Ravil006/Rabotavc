import sqlite3
connection = sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('SELECT COUNT(*) FROM users')
total_users=cursor.fetchone()[0]
print('общее количество пользователей: ', total_users)
connection.close()