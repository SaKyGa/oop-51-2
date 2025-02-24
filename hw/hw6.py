import sqlite3

connect = sqlite3.connect('User.db')

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
            ''')

connect.commit()



def add_user(name, age, hobby):
    
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")



add_user("ardager", 23, "плавать")
add_user("Arsen", 17, "read books")
add_user("Aidana", 21, "dance")


def get_all_users():
    
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    print(users)
    print('Список всех пользователей')
    
    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
        
get_all_users()

def get_users_by_name():

    name = input("Введите имя пользователя: ")

    conn = sqlite3.connect('User.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, age, hobby FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()

    conn.close()
    
    if user:
        print(f"NAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print("Пользователь не найден")

get_users_by_name()
    