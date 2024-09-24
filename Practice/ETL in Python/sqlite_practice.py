import sqlite3

conn = sqlite3.connect("Practice/ETL in Python/database_test.db")
cursor = conn.cursor()
cursor.execute("""create table people(id integer primary key, name text(50), age integer)""")
cursor.execute("""insert into people (name, age) values (?, ?)""", ("Lawrence", 25))
cursor.execute("""insert into people (name, age) values (?, ?)""", ("Johanna", 24))
# conn.commit()
# conn.close()

result = cursor.execute("select * from people")
data = result.fetchall()
print(data)
