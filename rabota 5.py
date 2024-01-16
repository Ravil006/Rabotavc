import sqlite3
connection = sqlite3.connect('my_database.db')
cursor=connection.cursor()
cursor.execute('DELETE FROM Users WHERE username=?',('newuser',))
connection.commit()
connection.close()