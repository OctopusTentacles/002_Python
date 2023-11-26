# Задача 1. Работа с файлом 2
# Реализуйте модернизированную версию контекст-менеджера File: 

# теперь при попытке открыть несуществующий файл менеджер должен автоматически 
# создавать и открывать этот файл в режиме записи; 
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.

import os

class File:
    def __init__(self, file_name: str, mode: str = "r") -> None:
        """ контекст-менеджер File - при попытке открыть несуществующий 
            файл - автоматически создает  и открывает этот файл в режиме записи
        """
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        """ метод для входа в блок контекст-менеджера.
            :cur_dir: каталог для работы с файлами.
        """
        cur_dir = os.path.join(os.path.dirname(__file__), self.file_name)

        try:
            # открываем файл для чтения
            self.file = open(cur_dir, self.mode, encoding="utf8")
            # print("файл открыт для чтения!")

        except FileNotFoundError: 
            # но если файл не существует - создаем и открываем для записи
            self.file = open(cur_dir, "w", encoding="utf8")
            # print("файл создан и открыт для записи!")

        return self.file

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """ метод для выхода из блока контекст-менеджера
        """
        # подавление всех исключений
        return True 


with File("example.txt") as file:
    file.write("Всем привет!")
