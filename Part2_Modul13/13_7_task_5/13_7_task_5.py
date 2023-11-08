# Задача 5. Обработка логов
# Контекст
# Вы работаете в большой компании, которая обслуживает сложную систему торговли. 
# Каждый день генерируется огромное количество лог-файлов, содержащих информацию о 
# торговых операциях. Вам поставлена задача разработать программу, которая будет 
# автоматически анализировать эти лог-файлы и находить строки с сообщениями об 
# ошибках (ERROR). Это поможет вам быстро отслеживать проблемы в торговой 
# системе и эффективно на них реагировать.

# Задача
# Напишите программу, которая считывает строки из файла и выводит строки, 
# содержащие слово ERROR, в новый файл.

# Требования
# Создайте функцию-генератор error_log_generator, которая будет получать на 
# вход путь до файла с логами и возвращать строки из этого файла, которые содержат слово 
# ERROR (одно обращение к генератору должно возвращать одну строку из файла).
# Советы
# Цикл for по файлу будет считывать в память ровно по одной строке из файла за итерацию.
# Генератор должен возвращать только строки со словом ERROR. Другие строки, 
# которые будут считываться из файла, нужно будет игнорировать 
# (применять yield только к правильным строкам).
# Для наглядного примера вы можете сгенерировать очень большой текстовый файл 
# (для этого надо запустить код из файла text_generator.py) и попробовать загрузить 
# его в память при помощи метода read(), применённого к этому файлу.
# Учтите, что генерация файла такого размера может занять несколько десятков минут!


# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt 
# и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = ...
output_file_path = ...
# Документация по join 
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/

# with open(output_file_path, 'w') as output:
#     for error_line in error_log_generator(input_file_path):
#         output.write(error_line)
# print("Файл успешно обработан.")


import os


def find_file(cur_path, dir_name):
    for dirpath, dirnames, filenames in os.walk(cur_path):
        for dirname in dirnames:
            if dirname == dir_name:
                return os.path.join(dirpath, dirname)

def check_exist(cur_path):
    try:
        if os.path.exists(cur_path):
            print("путь найден")
            return cur_path
        else: raise Exception
    except Exception as exc:
        print("Директории не существует", type(exc))


# директория скрипта
cur_dir = os.path.dirname(__file__)
# директория рабочих файлов
dir_name = find_file(cur_dir, "data")

input_file_path = check_exist(os.path.join(dir_name, "work_logs.txt"))


print("файл лежит тут:", input_file_path)
