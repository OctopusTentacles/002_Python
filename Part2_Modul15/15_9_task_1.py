# Задача 1. Работа с файлом 2
# Реализуйте модернизированную версию контекст-менеджера File: 

# теперь при попытке открыть несуществующий файл менеджер должен автоматически 
# создавать и открывать этот файл в режиме записи; 
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.

import os

class File:
    def __init__(self, file_name:str, mode:str = "a") -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        cur_dir = os.path.join(os.path.dirname(__file__), self.file_name)

        try:
            self.file = open(cur_dir, self.mode)

        except FileNotFoundError: 
            self.file = open(cur_dir, "w", encoding="utf8")

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return True # для исключения любых ошибок


with File("example.txt") as file:
    file.write("Всем привет!")
