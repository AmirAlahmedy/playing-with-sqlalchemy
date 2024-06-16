import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Movies(Title TEXT, Director TEXT, Year INT)''')
#cursor.execute('''INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorses', 1976) ''')

famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
               ('Back to the Future', 'Robert Zemeckis', 1985),
               ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# cursor.executemany('INSERT INTO Movies VALUES (?, ?, ?)', famousFilms)

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

# cursor.execute('''SELECT * FROM Movies''')

print(cursor.fetchall())

connection.commit()
connection.close()
