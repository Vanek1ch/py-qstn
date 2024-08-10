import tkinter as tk

# Это основное окно для работы с опросами


def main(user_id):
    # Основные параметры окна
    root = tk.Tk()
    root.title("Py-qstn")
    root.geometry("470x300+700+300")
    root.resizable(False, False)

    # Текст
    name_lic = tk.Label(text=f"ЛК:{user_id}")
    name_lic.place(x=200, y=200)

    root.mainloop()


if __name__ == "__main__":
    main()
