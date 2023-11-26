# Задача 1. Работа с файлом 2
# Реализуйте модернизированную версию контекст-менеджера File: 

# теперь при попытке открыть несуществующий файл менеджер должен автоматически 
# создавать и открывать этот файл в режиме записи; 
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.


class File:
    def __init__(self, file_name:str, mode:str = "w") -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding="utf8")
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


with File("example.txt", "r") as file:
    file.write()
