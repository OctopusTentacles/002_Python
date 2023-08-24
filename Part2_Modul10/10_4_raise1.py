# Задача 1. Имена
# В базе данных одной компании есть баг (или, может быть, фича): 
# если ввести туда имя сотрудника меньше чем из трёх букв, 
# то база сломается и упадёт. Как компания принимает на работу людей, 
# например, с китайскими именами, непонятно.

# Дан файл people.txt, в котором построчно хранится N имён пользователей. 

# Напишите программу, которая берёт количество символов в каждой 
# строке файла и в качестве ответа выводит общую сумму. 
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), 
# то вызывается ошибка, и программа завершается.

import os


def open_file(cur_path, file_name):
    
    try:
        open_file = open(os.path.join(cur_path, file_name), 'r', encoding='utf8')
    except FileNotFoundError as exc:
        print(type(exc), 'Нет такого файла или директории')

    else:
        total_sym = 0
        for i_line in open_file.readlines():
            sym_in_line = 0
            for i_sym in i_line:
                if i_sym.isalpha():
                    sym_in_line += 1
                    total_sym += 1
            print('в строке', sym_in_line, 'символов')
            
            if sym_in_line < 3:
                print('вызывается ошибка, и программа завершается')

        print('общее число символов:', total_sym)
        
    finally:
        if not open_file.closed:
            open_file.close()
            print('файл закрылся')
    




cur_dir = os.path.dirname(__file__)

open_file(cur_dir, 'people.txt')