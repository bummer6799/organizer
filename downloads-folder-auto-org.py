import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import plyer
import time


def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    root.destroy()
    # notification = plyer.notification.Notification(
    #     title="File Organizer",
    #     message="Running in the background...",
    #     app_name="File Organizer"
    # )
    # notification.show()


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
            src = os.path.join(folder_path, file)
            dst = os.path.join(folder_path, file_type + 's', file)
            shutil.move(src, dst)
            # notification = plyer.notification.Notification(
            #     title="File Moved",
            #     message=f"{file} was moved to {dst}",
            #     app_name="File Organizer",
            #     timeout=5
            # )
            # notification.add_action(
            #     label="Open Folder",
            #     action=lambda: os.startfile(folder_path)
            # )
            # notification.show()


root = tk.Tk()
root.title("File Organizer")

folder_path = None

select_folder_button = tk.Button(text="Select Folder", command=select_folder)
select_folder_button.pack()

root.mainloop()

while True:
    time.sleep(1)
    if folder_path:
        organize_folder(folder_path)