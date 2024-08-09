import sqlite3

# Тут находятся все функции, которые оперируют над базами данных и инициализация этих баз


def check_user(login, password):
    # Устанавливаем соединение с БД
    conn = sqlite3.connect("py-qstn/users_database.db")
    cur = conn.cursor()

    # Создаем таблицу Users
    cur.execute(""" CREATE TABLE IF NOT EXISTS Users 
                (
                user_id INTEGER PRIMARY KEY,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                email TEXT NOT NULL,
                is_admin INTEGER NOT NULL,
                birth_date DATE NOT NULL,
                age INTEGER NOT NULL
                )
                """)
    conn.commit()

    # Делаем запрос на извлечение данных
    cur.execute(""" SELECT * FROM Users
                WHERE login = ?
                AND password = ?
                """, (login, password))

    # Цепляем все данные пользователя если он существует
    user = cur.fetchone()

    # Закрываем соединение с БД
    conn.close()

    return user
