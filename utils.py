import os
import time
import datetime
from shutil import move, rmtree
from tkinter import *
from tkinter import ttk

def clear_empty_folders(path: str) -> None:
    """
        Recurse function for deleting empty folders from destination path
    """
    for element in os.listdir(path):
        new_path = os.path.join(path, element)
        if os.path.isdir(new_path):
            clear_empty_folders(new_path)
    
    if len(os.listdir(path)) == 0:
        try:
            rmtree(path)
        except:
            pass

def how_much_files(path: str, counter: int = 0) -> int:
    """
        Scanning path and return how much files in directory and all subdirectories
    """
    for element in os.listdir(path):
        path_to_element = os.path.join(path, element)
        
        if os.path.isdir(path_to_element):
            counter = how_much_files(path_to_element, counter)
        else:
            counter += 1
    
    return counter

def extract_files_from_path(path: str, destination_path: str,
                            days: int, progressbar: ttk.Progressbar,
                            divider_length: float, frame: ttk.Frame,
                            log_row: Label, counter: int) -> None:
    """
        Recurse function for moving files to new path
    """
    # Creating needed folder if it's not created yet
    try:
        os.mkdir(destination_path)
    except:
        pass
    
    # Collecting files in directory, if founds folder - going into it
    for element in os.listdir(path):
        path_to_element = os.path.join(path, element)
        if os.path.isdir(path_to_element):
            new_path = os.path.join(destination_path, element)

            counter = extract_files_from_path(path_to_element, new_path,
                                                days, progressbar,
                                                divider_length, frame,
                                                log_row, counter)
        else:
            progressbar['value'] += divider_length
            frame.update()

            # Getting days passed from last accessed date
            dt = datetime.datetime.fromtimestamp(
                    time.mktime(
                        time.localtime(
                            os.path.getatime(path_to_element)
                        )
                    )
                )
            days_passed = (datetime.datetime.now() - dt).days

            # Moving file if it's satisfies conditions
            if days_passed > days:
                counter += 1

                text = f"""Перемещается {element}
                Пожалуйста, подождите!
                Не закрывайте это окно
                """

                log_row.configure(text=text)
                frame.update()

                move(path_to_element, destination_path)
    
    # Remove folder if it's empty
    if len(os.listdir(path)) == 0:
        try:
            rmtree(path)
        except:
            pass

    return counter

def copy_files(start_path: str, end_path: str, passed_days: int, log_row: Label, frame: Tk) -> int:
    """
        start_path: C:\\path\\to\\source

        end_path: D:\\path\\to\\folder

        ends with D:\\path\\to\\folder\\path\\to\\source

        Returns how much files was founded
    """
    destination_path = os.path.join(end_path, '\\'.join(start_path.split('\\')[1:]))
    destination_path_list = destination_path.split("\\")

    # Recreating all tree in new directory
    creation_path = destination_path_list[0]
    for folder in destination_path_list[1:]:
        creation_path += f"\\{folder}"
        try:
            os.mkdir(creation_path)
        except:
            pass
    
    counter = 0
    value_var = IntVar(value=0)
    
    how_much_files_value = how_much_files(start_path)
    if how_much_files_value == 0: return 0
    
    # Getting progressbar divider
    divider_length = 100/how_much_files_value

    progressbar = ttk.Progressbar(frame, orient="horizontal", variable=value_var, length=100)
    progressbar.grid(column=0, row=1, padx=2, pady=2)

    counter = extract_files_from_path(start_path, destination_path, passed_days,
                            progressbar, divider_length, frame, log_row, counter)

    text = "Производится удаление пустых папок"
    log_row.configure(text=text)
    frame.update()

    clear_empty_folders(destination_path)

    return counter
