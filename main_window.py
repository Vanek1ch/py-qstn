import tkinter as tk
import bd_func as bd

# Это основное окно для работы с опросами


def main(name, surname):
    # Основные параметры окна
    root = tk.Tk()
    root.title("Py-qstn")
    root.geometry("470x300+700+300")
    root.resizable(False, False)

    # Текст
    name_lic = tk.Label(text=f"ЛК:{name} {surname}")
    name_lic.place(x=470-(100+len(name+surname)), y=20)

    # Кнопки
    solve_test_button = tk.Button(text="Пройти тестирование")
    solve_test_button.place(x=150, y=250)

    # Combo box

    # qstn_box = tk.Combobox(textvariable=)

    root.mainloop()


if __name__ == "__main__":
    main()
