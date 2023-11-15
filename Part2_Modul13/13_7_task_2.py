# Задача 2. Пути файлов
# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам 
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем 
# каталог и генерирует пути всех встреченных файлов. 
# В решении не нужно использовать рекурсию.

# Подсказка: вместо написания кода с рекурсией используйте готовую 
# рекурсивную функцию os.walk() — os — Miscellaneous operating system interfaces — 
# Python 3.11.0 documentation.


import os


# def gen_files_path(folder_name: str) -> str:
#     """ gen_files_path - находит указанный пользователем каталог 
#         и генерирует пути файлов в нем.
#     """
#     # print(os.path.abspath(folder_name))
#     for dirpath, dirnames, filenames in os.walk("/"):
#         if folder_name in dirpath:
#                 for filename in filenames:
#                     yield "\tФайл: ", os.path.join(dirpath, filename)


# catalog = gen_files_path(input("Имя каталога: "))

# for dir in catalog:
#     print(*dir)


# def root_path() -> str:
#     return os.path.abspath(os.sep)

# def gen_files_path(folder: str, path=os.path.abspath(os.sep)):
#     for root, dirs, files in os.walk(path):
#         print(root, dirs, files)
#         for file in files:
#             yield os.path.join(root, file)
#         if folder in dirs:
#             print(f'Искомая директория {folder} найдена {os.path.join(root, folder)}')
#             return True


# current_folder = os.path.abspath(os.sep)
# print(current_folder)

# for file_path in gen_files_path(current_folder):
#     print(file_path)

# 12_7_task_4


def gen_files_path(folder_name: str, path=os.path.abspath(os.sep)):
    for root, dirs, files in os.walk(path):
        if folder_name in root:
            for file in files:
                yield "\tФайл: ", os.path.join(root, file)


catalog = input("Имя каталога: ")
for file_path in gen_files_path(catalog):
    print(*file_path)

