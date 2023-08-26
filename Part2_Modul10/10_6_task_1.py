# Задача 1. Имена 2
# Что нужно сделать
# Есть файл people.txt, в котором построчно хранится N имён пользователей. 
# Напишите программу, которая берёт количество символов в каждой строке 
# файла и в качестве ответа выводит общую сумму. 
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), 
# то вызывается ошибка и сообщение, в какой именно строке она возникла. 
# Программа при этом не завершается и обрабатывает все имена файла.

# Также при желании можно вывести все ошибки в отдельный файл errors.log.
# Пример работы программы
# Содержимое файла people.txt:
# Василий
# Николай
# Надежда
# Никита
# Ян
# Ольга
# Евгения
# Кристина

# Ответ в консоли:
# Ошибка: менее трёх символов в строке 5.
# Общее количество символов: 49.

import os


def open_file(cur_dir, file_name):
    amt_sym = 0
    error_line = 0
    with open(os.path.join(cur_dir, file_name), 'r', encoding='utf8') as r_file, \
        open(os.path.join(cur_dir, 'errors.log'), 'w', encoding='utf8') as w_file:
        
            for i_line in r_file:
                try:
                    error_line += 1
                    sym_in_line = len(i_line.rstrip())
                    amt_sym += sym_in_line
                    if sym_in_line < 3:
                        raise BaseException('Ошибка: менее трёх символов в строке {}'\
                                         .format(error_line))
                
                except BaseException as exc:
                    print(exc)
                    w_file.write(f'{str(exc)}\n')     
                
            print('Общее количество символов:', amt_sym)


# текущая директория
current_dir = os.path.dirname(__file__)

# открыть файл и прочитать строки
open_file(current_dir, 'people.txt')