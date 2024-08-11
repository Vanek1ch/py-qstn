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
                patronymic TEXT NOT NULL,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                edu_inst TEXT NOT NULL,
                email TEXT NOT NULL,
                is_admin INTEGER,
                birth_date DATE NOT NULL
                )
                """
                )
    # Подтверждаем изменения
    conn.commit()
    conn.close()

# Работа с бд опросников, вопросов, ответов


def SQC_db():

    conn = sqlite3.connect("py-qstn/qstn_database.db")
    cur = conn.cursor()

    # Таблица для вопросников
    cur.execute("""
                CREATE TABLE IF NOT EXISTS surveys
                (
                    survey_id INTEGER PRIMARY KEY,
                    survey_name TEXT NOT NULL,
                    survey_author TEXT NOT NULL,
                    survey_description TEXT NOT NULL,
                    survey_time TEXT NOT NULL
                )
                """)

    # Таблица для вопросов
    cur.execute("""
                CREATE TABLE IF NOT EXISTS questions
                (
                    question_id INTEGER PRIMARY KEY,
                    survey_id INTEGER,
                    question_text TEXT NOT NULL,
                    question_type TEXT NOT NULL,
                    FOREIGN KEY (survey_id) REFERENCES surveys(survey_id)
                )
                """)

    # Таблица для вариантов ответа
    ''' реализовать
    cur.execute("""
                CREATE TABLE IF NOT EXISTS choices 
                (
                 choice_id INTEGER PRIMARY KEY,
                 question_id INTEGER,
                 choice_text TEXT NOT NULL,
                 FOREIGN KEY (question_id) REFERENCES questions(questions_id)   
                )
                """)
    '''

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
        SELECT name, surname FROM Users
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
    cur.execute(
        """
        INSERT INTO Users 
        (
        login, password, name, surname, patronymic, edu_inst, email,
        birth_date
        ) 
        VALUES (?,?,?,?,?,?,?,?)
        """, args
    )
    conn.commit()
    conn.close()

# Функция создающая список доступных для прохождения тестов


def tuple_of_surveys():

    SQC_db()

    conn = sqlite3.connect("py-qstn/qstn_database.db")
    cur = conn.cursor()

    # Делаем запрос на получение данных
    cur.execute(
        """
        SELECT survey_name from surveys
        """
    )

    survey_tuple = cur.fetchall()

    conn.close()

    return survey_tuple
