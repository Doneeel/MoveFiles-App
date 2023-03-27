from tkinter import *
from tkinter import filedialog
import os

from utils import copy_files

def save_directory(lbl: Label):
    path_entry = filedialog.askdirectory().replace("/", "\\")
    
    if path_entry != "":
        lbl.configure(text=path_entry)

def validate_moving(start_path: Label, end_path: Label, days: Entry, 
                    log_row: Label, window: Tk):
    try:
        start_path = start_path.cget("text")
        end_path = end_path.cget("text")

        if not os.path.exists(start_path) or not os.path.exists(end_path):
            print(0/0)

        days = int(days.get())
    except:
        log_row.configure(text="Что-то пошло не так,\nне указано количество дней (или указано не число)\nи/или начальный путь и/или конечный путь")
        return
    
    window.iconify()

    # Generates new temp frame for progressbar and info 
    frame = Tk()
    frame.title("Идет процесс")

    frame.geometry('400x100')
    frame.configure(bg='white')

    process_log_row = Label(frame, text="Процесс начинается", bg="white")
    process_log_row.grid(column=0, row=0, padx=2, pady=2)

    frame.update()
    files_counter = copy_files(start_path, end_path, days, process_log_row, frame)

    frame.destroy()
    window.deiconify()
    log_row.configure(text=f"Перенос завершен\nПеренесено: {files_counter} файлов")


def generate_window() -> Tk:
    window = Tk()
    x_padding = 150

    window.geometry('400x300')
    window.configure(bg='white')

    window.title("Скрипт для переноса файлов")

    lbl_start_path = Label(window, text="Начальный путь", bg="white")
    lbl_start_path.grid(column=1, row=0, padx=x_padding, pady=2)

    choose_path = Button(window, text="Выбрать путь", command=lambda: save_directory(lbl_start_path), bg="white")
    choose_path.grid(column=1, row=1, padx=x_padding, pady=2)

    lbl_end_path = Label(window, text="Конечный путь", bg="white")
    lbl_end_path.grid(column=1, row=2, padx=x_padding, pady=2)

    choose_path = Button(window, text="Выбрать путь", command=lambda: save_directory(lbl_end_path), bg="white")
    choose_path.grid(column=1, row=3, padx=x_padding, pady=2)

    lbl_days = Label(window, text="Больше ... дней", bg="white")
    lbl_days.grid(column=1, row=4, padx=x_padding, pady=2)

    days_entry = Entry(window, width=10, bg="#F9F9F9")
    days_entry.grid(column=1, row=5, padx=x_padding, pady=2)

    log_row = Label(window, text="None", bg="white")
    log_row.grid(column=1, row=6, padx=25, pady=10)

    btn = Button(window, text="Запустить", command=lambda: validate_moving(lbl_start_path, lbl_end_path, days_entry, log_row, window), bg="white")
    btn.grid(column=1, row=7, padx=x_padding, pady=2)

    return window

def main():
    window = generate_window()
    window.mainloop()

if __name__ == '__main__':
    main()
    