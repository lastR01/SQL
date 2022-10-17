import sqlite3
import random

global db
global sql
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    telephone BIGINT,
    money BIGINT
)""")
db.commit()

def reg():
    user_login = input('Логин: ')
    user_password = input('Пароль: ')
    user_telephone = input('Телефон: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES(?, ?, ?, ?)", (user_login, user_password, user_telephone, 0))
        db.commit()
        print('Зарегистрировано!')
        print("Все данные: ")
        for data in sql.execute("SELECT * FROM users"):
            print(data)
    else:
        print('Такая запись уже имеется!')
        for value in sql.execute("SELECT login, telephone FROM users"):
            print(value)


def casino():
    user_login = input('Login: ')
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print('Такого логина не существует! Зарегистрируйтесь!')
        reg()
    else:
        choice = int(input('Введите число на которое хотите поставить(от 1 до 3): '))
        win_number = random.randint(1, 3)
        print("Выигрышное число:", win_number)
        if choice == win_number:
            print('Поздравляем, вы выиграли!!!')
            sql.execute(f"UPDATE users SET money = money + {1000} WHERE login = '{user_login}'")
            db.commit()
        else:
            print('Вы проиграли!')

        for players in sql.execute(f'SELECT login, telephone, money FROM users'):
            print(players)

casino()
input()