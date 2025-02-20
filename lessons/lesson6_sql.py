# import sqlite3

# # A4
# connect = sqlite3.connect('User.db')

# # Рука с Ручкой
# cursor = connect.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         name VARCHAR (40) NOT NULL,
#         age INTEGER NOT NULL,
#         hobby TEXT
#     )
#             ''')


# # Сохранение изменений
# connect.commit()


# # CRUD - Create - Reate - Update - Delete

# # Create
# def add_user(name, age, hobby):
    
#     cursor.execute(
#         'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
#         (name, age, hobby)
#     )
#     connect.commit()
#     print(f"Пользователь {name} добавлен")

# # name = input("Введите имя")
# # age = input("Введите возраст")
# # hobby = input("Введите Хоби")

# add_user("ardager", 23, "плавать")


# def get_all_users():
    
#     cursor.execute('SELECT name, age, hobby FROM users')
#     users = cursor.fetchall()
#     print(users)
#     print('Список всех пользователей')
    
#     for i in users:
#         print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
        
        
        
# get_all_users()






import sqlite3

conn = sqlite3.connect("User.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = OFF;")  # Отключаем внешние ключи на время удаления
cursor.execute("BEGIN TRANSACTION;")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    cursor.execute(f"DELETE FROM {table[0]};")  # Очищаем таблицу
    # Убираем сброс автоинкремента, так как его нет

cursor.execute("COMMIT;")
cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем обратно

conn.commit()
conn.close()

print("База данных очищена, но структура таблиц сохранена.")