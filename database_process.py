# Arda Mavi
# Импорт необходимых библиотек
import os
import sqlite3

# Функция для создания подключения к базе данных
def set_sql_connect(database_name):
    return sqlite3.connect(database_name)

# Функция для создания курсора для выполнения SQL-запросов
def set_sql_cursor(database_connect):
    return database_connect.cursor()

# Функция для закрытия соединения с базой данных
def close_connect(vt):
    if vt:
        vt.commit()
        vt.close()

# Функция для установки соединения и создания курсора
def set_connect_and_cursor(path='Data/database.sqlite'):
    vt = set_sql_connect(path)
    db = set_sql_cursor(vt)
    return vt, db

# Функция для создания таблицы в базе данных
def create_table(table_name, columns):
    vt, db = set_connect_and_cursor()
    # Выполнение команды для создания таблицы, если она не существует
    db.execute("CREATE TABLE IF NOT EXISTS {0} ({1})".format(table_name, columns))
    close_connect(vt)

# Функция для получения данных из базы данных по SQL-команде
def get_data(sql_command):
    vt, db = set_connect_and_cursor()
    db.execute(sql_command)
    gelen_veri = db.fetchall()
    close_connect(vt)
    return gelen_veri

# Функция для добавления данных в таблицу
def add_data(table, adding):
    vt, db = set_connect_and_cursor()
    # Выполнение команды вставки данных в указанную таблицу
    db.execute("INSERT INTO '{0}' VALUES ({1})".format(table, adding))
    close_connect(vt)
    