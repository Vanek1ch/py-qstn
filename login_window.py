import tkinter as tk
import bd_func as bd
import registration_window as rw
import main_window as mw

# Создание окна регистрации/логина


def main():
    root = tk.Tk()

    # Вывод сообщения об ошибке
    # Типы:
    # UPI - Username or Password is Incorrect
    def err_msg(type):
        if type == "UPI":
            err_text = tk.Label(text="Неправильно введен Логин или Пароль")
            err_text.place(x=120, y=240)

    # Настройки окна
    root.title("Py-qstn")
    root.geometry("470x300+700+300")
    root.resizable(False, False)

    # Поля ввода
    login_entry = tk.Entry()
    login_entry.place(x=150, y=60)

    password_entry = tk.Entry(show="*")
    password_entry.place(x=150, y=120)

    # Текст
    login_text = tk.Label(text="Login:")
    login_text.place(x=100, y=60)

    password_text = tk.Label(text="Password:")
    password_text.place(x=80, y=120)

    # Функция кнопки входа
    def login():
        # Получение логина и пароля
        login = login_entry.get()
        password = password_entry.get()

        # Обращение к БД
        name, surname = bd.check_user(login, password)

        if name is None:
            err_msg("UPI")
        else:
            root.destroy()
            mw.main(name, surname)

    # Функция кнопки регистрации

    def registration():
        root.destroy()
        rw.main()

    # Кнопки
    login_button = tk.Button(text="Войти", command=login)
    login_button.place(x=150, y=200)

    registration_button = tk.Button(text="Регистрация", command=registration)
    registration_button.place(x=250, y=390)

    root.mainloop()


if __name__ == "__main__":
    main()
