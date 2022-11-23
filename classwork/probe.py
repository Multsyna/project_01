# СОЗДАНИЕ ТАБЛИЦЫ
import sqlite3


connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students 
( 
  Student_Id INTEGER NOT NULL, 
  Student_Name TEXT NOT NULL,
  School_Id INTEGER NOT NULL PRIMARY KEY 
);
"""
cursor.execute(query)
connection.commit()
connection.close()    


