import sqlite3

# Тут находятся все функции, которые оперируют над базами данных и инициализация этих баз


def main():
    # Устанавливаем соединение с БД
    conn = sqlite3.connect("py-qstn/users_database.db")
    cur = conn.cursor()

    # Создаем таблицу Users
    cur.execute("""
                CREATE TABLE IF NOT EXISTS Users 
                (
                user_id INTEGER PRIMARY KEY,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                edu_inst TEXT NOT NULL,
                email TEXT NOT NULL,
                is_admin INTEGER NOT NULL,
                birth_date DATE NOT NULL,
                age INTEGER NOT NULL
                )
                """)
    # Подтверждаем изменения
    conn.commit()
    conn.close()

# Функция проверки пользователя на сущетсвование в базе данных


def check_user(login, password):

    main()

    # Устанавливаем соединение с БД
    conn = sqlite3.connect("py-qstn/users_database.db")
    cur = conn.cursor()

    # Делаем запрос на извлечение данных
    cur.execute(
        """
        SELECT * FROM Users
        WHERE login = ?
        AND password = ?
        """, (login, password))

    # Цепляем все данные пользователя если он существует
    user = cur.fetchone()

    # Закрываем соединение с БД
    conn.close()

    # Возвращаем данные пользователя
    return user


# Функция добавления пользователя в базу данных
def add_user(*args):

    main()

    # Устанавливаем соединение с БД
    conn = sqlite3.connect("py-qstn/users_database.db")
    cur = conn.cursor()

    # Делаем запрос на внесение данных
    cur.execute
    (
        """
        INSERT INTO Users 
        (
        login, password, name, surname, edu_inst, email, 
        is_admin, birth_date, age
        ) 
        VALUES (?,?,?,?,?,?,?,?,?)
        """, (args)
    )
    conn.commit()
    conn.close()
