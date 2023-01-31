import os
import shutil

folder_path = r"C:\Users\Lenovo\Downloads"  # replace with your folder path

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

organize_folder(folder_path)
