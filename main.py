import tkinter as tk
from tkinter import filedialog
import os
import shutil


def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path


def organize_folder(folder_path):
    files = os.listdir(folder_path)
    file_types = set()

    for file in files:
        file_type = os.path.splitext(file)[1][1:]
        if file_type:
            file_types.add(file_type)

    for file_type in file_types:
        type_folder = os.path.join(folder_path, file_type + 's')
        if not os.path.exists(type_folder):
            os.makedirs(type_folder)

    for file in files:
        file_type = os.path.splitext(file)[1][1:]
        if file_type:
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, file_type + 's', file))


root = tk.Tk()
root.title("File Organizer")

select_folder_button = tk.Button(text="Select Folder", command=select_folder)
select_folder_button.pack()

organize_folder_button = tk.Button(text="Organize Folder", command=lambda: organize_folder(select_folder()))
organize_folder_button.pack()

root.mainloop()