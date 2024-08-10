import tkinter as tk
import bd_func as bd


def main():
    # Инициализация окна
    root = tk.Tk()

    # Параметры окна
    root.title("Py-qstn")
    root.geometry("470x300+700+300")
    root.resizable(False, False)

    # Функция регистрации
    def registration():

        # Данные для БД
        login = login_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        name = name_entry.get()
        surname = surname_entry.get()
        patronymic = patronymic_entry.get()
        birth_date = birth_date_entry.get()
        edu_inst = edu_inst_entry.get()

        # Обращение к БД для добавления пользователя
        bd.add_user(login, password, name, surname, patronymic, edu_inst, email,
                    birth_date)
    # Поля ввода
    login_entry = tk.Entry()
    login_entry.place(x=60, y=10)

    password_entry = tk.Entry()
    password_entry.place(x=60, y=30)

    email_entry = tk.Entry()
    email_entry.place(x=60, y=50)

    name_entry = tk.Entry()
    name_entry.place(x=60, y=70)

    surname_entry = tk.Entry()
    surname_entry.place(x=60, y=90)

    patronymic_entry = tk.Entry()
    patronymic_entry.place(x=60, y=110)

    birth_date_entry = tk.Entry()
    birth_date_entry.place(x=100, y=130)

    edu_inst_entry = tk.Entry()
    edu_inst_entry.place(x=100, y=150)

    # Текст
    login_text = tk.Label(text="Логин:")
    login_text.place(x=0, y=10)

    password_text = tk.Label(text="Пароль:")
    password_text.place(x=0, y=30)

    email_text = tk.Label(text="Почта:")
    email_text.place(x=0, y=50)

    name_text = tk.Label(text="Имя:")
    name_text.place(x=0, y=70)

    surname_text = tk.Label(text="Фамилия:")
    surname_text.place(x=0, y=90)

    patronymic_text = tk.Label(text="Отчество:")
    patronymic_text.place(x=0, y=110)

    birth_date_text = tk.Label(text="Дата Рождения:")
    birth_date_text.place(x=0, y=130)

    edu_inst_text = tk.Label(text="Учеб. Учржд.:")
    edu_inst_text.place(x=0, y=150)

    # Кнопки
    registration_button = tk.Button(
        text="Зарегистрироваться", command=registration)
    registration_button.place(x=180, y=200)

    root.mainloop()


if __name__ == "__main__":
    main()
