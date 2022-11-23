# Создание таблицы School
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE School 
(
School_Id INTEGER NOT NULL PRIMARY KEY, 
School_Name TEXT NOT NULL, 
Place_Count INTEGER NOT NULL
);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Наполнение таблицы School
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO School (School_Id, School_Name, Place_Count) 
VALUES 
('1', 'Протон', 200), 
('2', 'Преспектива', 300), 
('3', 'Спектр', 400), 
('4', 'Содружество', 500);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Создание таблицы Teacher
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE Teatcher 
( 
  Teatcher_Id INTEGER NOT NULL PRIMARY KEY, 
  Teatcher_Name TEXT NOT NULL, 
  School_Id INTEGER NOT NULL, 
  Joining_Date TEXT NOT NULL, 
  Speciality TEXT NOT NULL, 
  Salary INTEGER NOT NULL,
  Experience INTEGER
);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Наполнение таблицы Teacher
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO Teatcher (Teatcher_Id, Teatcher_Name, School_Id, Joining_Date, Speciality, Salary, Experience) 
VALUES 
('101', 'Галина', '1', '2021-2-10', 'Физик', '40000', NULL), 
('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL), 
('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL), 
('104', 'Полина', '2', '2017-12-28', 'Физик ', '28000', NULL), 
('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL), 
('106', 'Анастасия', '3', '2019-09-11', 'Учитель трудов', '30000', NULL), 
('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000', NULL), 
('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Общение с БД
import sqlite3

connection = sqlite3.connect('teatchers.db') # Подключаюсь к БД
cursor = connection.cursor() # Определяю Курсор
query = "SELECT * FROM School;" # Задаю переменную с SQL запросом
cursor.execute(query) # С помощью курсора выполняю SQL запрос
record = cursor.fetchall() # Вывожу все результаты в переменную record (кортеж списков)
connection.close() # Отключаюсь от БД
print (record)

import sqlite3

connection = sqlite3.connect('test.db')




# 17.11.22




import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_db():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = ("SELECT sqlite_version();")
    cursor.execute(query)
    version = cursor.fetchone()
    print ("Вы подключились к версии ", version)
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных ", error)

print ("Задача №2 Версия БД")
read_db()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def insert_experience():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    update_query = ("UPDATE Teatcher SET Experience = 5 WHERE Experience IS NULL")
    cursor.execute(update_query)
    connection.commit()
    connection.close()
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных ", error)

print ("Задача 3 Апдейт опыта работы")
insert_experience()
print ("Опыт обновлен")

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_detail(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    records = cursor.fetchall()
    print ("Данные по школе")
    for row in records:
      print ("ID школы", row[0])
      print ("Название школы", row[1])
      print ("Количество мест", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

def get_teatcher_detail(teatcher_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Teatcher WHERE Teatcher_Id = ?"""
    cursor.execute(select_query, (teatcher_id,))
    records = cursor.fetchall()
    print ("Данные по учителю")
    for row in records:
      print ("ID учителя", row[0])
      print ("Имя учителя", row[1])
      print ("ID школы", row[2])
      print ("Дата начала работы", row[3])
      print ("Специализация", row[4])
      print ("Зарплата", row[5])
      print ("Опыт работы", row[6]) 
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

print ("Задача 4 данные по учителю и школе")
get_school_detail(1)
print ("\n")
get_teatcher_detail(107)

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = ("SELECT * FROM Teatcher")
cursor.execute(query)
records = cursor.fetchall()

print(records)

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_teatchers_list(speciality, salary):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Teatcher WHERE Speciality = ? AND Salary > ?"""
    cursor.execute(select_query, (speciality,salary))
    records = cursor.fetchall()
    print ("Учитель со специальностью", speciality, "и зарплатой больше ", salary)
    for row in records:
      print ("ID учителя", row[0])
      print ("Имя учителя", row[1])
      print ("ID школы", row[2])
      print ("Дата начала работы", row[3])
      print ("Специализация", row[4])
      print ("Зарплата", row[5])
      print ("Опыт работы", row[6], "\n") 
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

print ("Задача 5 Список учителей \n")
get_teatchers_list("Физик", 30000)

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
    return record[1] # Наименование школы
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

def get_teacher(school_id):
  try:
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Teatcher WHERE School_Id = ?"""
    cursor.execute(select_query, (school_id,))
    records = cursor.fetchall()

    print ("Учителя из школы ", school_name)
    for row in records:
      print ("ID учителя", row[0])
      print ("Имя учителя", row[1])
      print ("ID школы", row[2])
      print ("Название школы", school_name)
      print ("Дата начала работы", row[3])
      print ("Специализация", row[4])
      print ("Зарплата", row[5])
      print ("Опыт работы", row[6], "\n") 
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

print ("Задача №6 \n")
get_teacher(3)