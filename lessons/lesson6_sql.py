import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')


# Сохранение изменений
connect.commit()


# CRUD - Create - Reate - Update - Delete



# Create
def add_user(name, age, hobby):
    
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

add_user("John", 33, "swimming")
add_user("samma", 23, "reading")
add_user("Wacka", 12, "dancing")

def get_all_users():

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)
    print("Все пользователи получены")

    for i in users:
        print(f"Name: {i[0]}, age: {i[1]}, hobby: {i[2]}")

get_all_users()