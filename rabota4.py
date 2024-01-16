import sqlite3
connection = sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))
connection.commit()
connection.close()
