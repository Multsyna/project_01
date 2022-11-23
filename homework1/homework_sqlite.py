import sqlite3


# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students 
# ( 
# Student_Id INTEGER NOT NULL, 
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY 
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

# import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id) 
# VALUES 
# ('201', 'Иван', 1), 
# ('202', 'Петр', 2),
# ('203', 'Анастасия', 3),
# ('204', 'Игорь', 4);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()
import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()
    
    
def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1] 
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)
    
def get_students(school_id):
  try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    records = cursor.fetchall()
    
    for row in records:
        print('Id студента: ', row[1])
        print('Имя студента: ', row[2]) 
        print('Id школы: ', row[0])
        print('Название школы: ', school_name)
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)
get_students(3)            






