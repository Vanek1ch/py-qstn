import tkinter as tk
import bd_func as bd
from tkinter import ttk
# Это основное окно для работы с опросами


def user(name, surname):
    # Основные параметры окна
    root = tk.Tk()
    root.title("Py-qstn")
    root.geometry("470x300+700+300")
    root.resizable(False, False)

    def start_test():
        root.destroy()

    # Текст
    name_lic = tk.Label(text=f"ЛК:{name} {surname}")
    name_lic.place(x=470-(100+len(name+surname)), y=20)

    # Кнопки
    solve_test_button = tk.Button(
        text="Пройти тестирование", command=start_test)
    solve_test_button.place(x=150, y=250)

    # Combobox
    tuple = bd.tuple_of_surveys()
    qstn_box = ttk.Combobox(values=tuple)
    qstn_box.place(x=20, y=20)

    root.mainloop()


def admin(name, surname):

    # Основные параметры окна
    root = tk.Tk()
    root.title("Py-qstn")
    root.geometry("470x300+700+300")
    root.resizable(False, False)

    def start_test():
        root.destroy()

    # Текст
    name_lic = tk.Label(text=f"ЛК:{name} {surname}")
    name_lic.place(x=470-(100+len(name+surname)), y=20)

    # Кнопки
    solve_test_button = tk.Button(
        text="Пройти тестирование", command=start_test)
    solve_test_button.place(x=150, y=250)

    # Combobox
    tuple = bd.tuple_of_surveys()
    qstn_box = ttk.Combobox(values=tuple)
    qstn_box.place(x=20, y=20)

    root.mainloop()


if __name__ == "__main__":
    user()
