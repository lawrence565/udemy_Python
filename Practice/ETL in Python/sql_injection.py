import sqlite3

conn = sqlite3.connect("Practice/ETL in Python/database_test.db")
name = input("Please enter your name: ")
cursor = conn.cursor()

#result = cursor.execute("select * from people")
result = cursor.execute("select * from people where name = '{}'".format(name))
data = result.fetchall()
print(data)