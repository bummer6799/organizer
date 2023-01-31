import tkinter as tk
from tkinter import filedialog
import os

def organize_folder():
    # get the folder path
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return

    # get all the file types in the folder
    files_in_folder = os.listdir(folder_selected)
    file_types = []
    for file in files_in_folder:
        if '.' in file:
            file_type = file.split('.')[-1]
            if file_type not in file_types:
                file_types.append(file_type)

    # create folders for each file type and move the respective files
    for file_type in file_types:
        folder_path = os.path.join(folder_selected, file_type + '_files')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for file in files_in_folder:
            if file.endswith('.' + file_type):
                file_path = os.path.join(folder_selected, file)
                new_file_path = os.path.join(folder_path, file)
                os.rename(file_path, new_file_path)

root = tk.Tk()
root.title("File Organizer")

# create and place the "Organize" button
btn = tk.Button(root, text="Organize", command=organize_folder)
btn.pack(fill='both', expand=True)

root.mainloop()
