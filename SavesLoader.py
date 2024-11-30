import os
import shutil
import tkinter as tk
from tkinter import messagebox, ttk

# Получаем имя пользователя
username = os.getlogin()

def create_save(save_index):
    src_dir = fr"C:\Users\{username}\AppData\LocalLow\Amistech\My Summer Car"
    dest_dir = os.path.join(os.getcwd(), f"Save{save_index}")

    # Создание директории для сохранения
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Копирование файлов
    for file_name in os.listdir(src_dir):
        full_file_name = os.path.join(src_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)

    messagebox.showinfo("Успех", f"Сохранение {save_index} создано.")

def load_save(save_index):
    src_dir = os.path.join(os.getcwd(), f"Save{save_index}")
    dest_dir = fr"C:\Users\{username}\AppData\LocalLow\Amistech\My Summer Car"

    # Проверка на существование директории с сохранением
    if not os.path.exists(src_dir):
        messagebox.showerror("Ошибка", f"Сохранение {save_index} не найдено.")
        return

    # Копирование файлов обратно
    for file_name in os.listdir(src_dir):
        full_file_name = os.path.join(src_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)

    messagebox.showinfo("Успех", f"Сохранение {save_index} восстановлено.")

def delete_saves():
    dir_to_delete = fr"C:\Users\{username}\AppData\LocalLow\Amistech\My Summer Car"

    # Проверка существования директории
    if not os.path.exists(dir_to_delete):
        messagebox.showerror("Ошибка", "Директория сохранений не найдена.")
        return

    # Удаление всех файлов и папок в директории
    for file_name in os.listdir(dir_to_delete):
        full_file_name = os.path.join(dir_to_delete, file_name)
        try:
            if os.path.isfile(full_file_name):
                os.remove(full_file_name)
            elif os.path.isdir(full_file_name):
                shutil.rmtree(full_file_name)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить {full_file_name}: {e}")
            return

    messagebox.showinfo("Успех", "Все сохранения удалены.")

def save_action():
    save_index = save_entry.get().strip()
    if save_index:
        create_save(save_index)
    else:
        messagebox.showwarning("Предупреждение", "Введите номер сохранения.")

def load_action():
    save_index = load_entry.get().strip()
    if save_index:
        load_save(save_index)
    else:
        messagebox.showwarning("Предупреждение", "Введите номер сохранения.")

def on_enter(event):
    event.widget['style'] = 'Hover.TButton'  # Изменение стиля кнопки при наведении

def on_leave(event):
    event.widget['style'] = 'TButton'  # Возврат к стандартному стилю кнопки

def main():
    global save_entry, load_entry

    # Создание основного окна
    root = tk.Tk()
    root.title("Сохранение и загрузка")
    root.geometry("400x400")
    root.resizable(False, False)

    # Настройка фона
    root.configure(bg="#2E2E2E")

    # Добавление рамки
    frame = tk.Frame(root, bg="#3E3E3E", bd=10, relief=tk.GROOVE)
    frame.pack(expand=True, fill=tk.BOTH)

    # Заголовок
    title_label = tk.Label(frame, text="Сохранение и загрузка", font=("Arial", 20, "bold"), bg="#3E3E3E", fg="#FFFFFF")
    title_label.pack(pady=10)

    # Поля для ввода
    tk.Label(frame, text="Номер сохранения для создания:", font=("Arial", 12), bg="#3E3E3E", fg="#FFFFFF").pack(pady=5)
    save_entry = ttk.Entry(frame, font=("Arial", 12), justify='center')
    save_entry.pack(pady=5)

    save_button = ttk.Button(frame, text="Сохранить", command=save_action)
    save_button.pack(pady=10)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    tk.Label(frame, text="Номер сохранения для загрузки:", font=("Arial", 12), bg="#3E3E3E", fg="#FFFFFF").pack(pady=5)
    load_entry = ttk.Entry(frame, font=("Arial", 12), justify='center')
    load_entry.pack(pady=5)

    load_button = ttk.Button(frame, text="Загрузить", command=load_action)
    load_button.pack(pady=10)
    load_button.bind("<Enter>", on_enter)
    load_button.bind("<Leave>", on_leave)

    delete_button = ttk.Button(frame, text="Удалить все сохранения", command=delete_saves)
    delete_button.pack(pady=10)
    delete_button.bind("<Enter>", on_enter)
    delete_button.bind("<Leave>", on_leave)

    exit_button = ttk.Button(frame, text="Выход", command=root.quit)
    exit_button.pack(pady=10)
    exit_button.bind("<Enter>", on_enter)
    exit_button.bind("<Leave>", on_leave)

    # Настройка стилей для кнопок
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10)
    style.configure("Hover.TButton", background="#4CAF50", font=("Arial", 12), padding=10)  # Стиль для кнопки при наведении
    style.map("TButton", background=[("active", "#3E3E3E")])  # Цвет кнопки при активном состоянии

    # Запуск основного цикла
    root.mainloop()

if __name__ == "__main__":
    main()