# Задача 1. Работа с файлом
# Реализуйте класс File — контекстный менеджер для работы с файлами. 
# Он должен принимать на вход имя файла и режим чтения/записи и открывать сам файл. 
# В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.

# Пример основного кода:

# with File(‘example.txt’, ‘w’) as file:
#     file.write(‘Всем привет!’)


class File:

    def __init__(self, file_name, mode) -> None:
        self.file = None
        self.file_name = file_name
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding="utf8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True # для исключения любых ошибок


with File("example.txt", "w") as file:
    file.write("Всем привет!")
