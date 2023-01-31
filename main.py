import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil


def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()


def organize_folder():
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder first")
        return

    if not messagebox.askokcancel("Organize Folder", "Are you sure you want to organize the selected folder?"):
        return

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
    messagebox.showinfo("Organize Folder", "The selected folder has been successfully organized")


root = tk.Tk()
root.title("File Organizer")

folder_path = None

select_folder_button = tk.Button(text="Select Folder", command=select_folder)
select_folder_button.pack()

organize_folder_button = tk.Button(text="Organize Folder", command=organize_folder)
organize_folder_button.pack()

root.mainloop()
