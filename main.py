import os
import tkinter as tk

#размер окна
widthHeight = [400, 300]

# Окно по центру
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

#Закрытие окна
def close_window():
    root.destroy()

# Обработка текста
def get_user_input():
    user_text = getTextUser.get()
    print("Полученный текст:", user_text)
    return user_text  # Возвращаем текст для использования

# Завершение процесса по имени
def kill_process_name():
    user_text = get_user_input()  # Получаем текст от пользователя
    os.system(f"taskkill /f /im {user_text}")

# Создание окна
root = tk.Tk()
root.title("Ручной Диспетчер")
window_width = widthHeight[0]
window_height = widthHeight[1]
center_window(root, window_width, window_height)
root.resizable(width=False, height=False)
root.config(bg='#616161')
root.iconbitmap('icon.ico')
# Ввод пользователя
getTextUser = tk.Entry(root)
getTextUser.pack()

# Кнопка получения текста
button = tk.Button(root, text="Получить процесс", command=get_user_input)
button.pack()

# Кнопка завершения процесса
kill = tk.Button(root, text="Убить процесс", command=kill_process_name)
kill.pack()

# Кнопка закрытия программы
closeButton = tk.Button(root, text="Закрыть", command=close_window)
closeButton.place(x=335, y=10)

# Запуск основного цикла обработки событий
root.mainloop()
