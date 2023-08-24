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

cur_dir = os.path.dirname(__file__)
line_count = 0
total_sym = 0
    
try:
    open_file = open(os.path.join(cur_dir, 'people.txt'), 'r', encoding='utf8')
    
    
    for i_line in open_file.readlines():
        line_count += 1
        sym_in_line = 0
        for i_sym in i_line:
            if i_sym.isalpha():
                sym_in_line += 1
                total_sym += 1
        print('в строке', sym_in_line, 'символов')
            
        if sym_in_line < 3:
           raise BaseException('Длина {} строки меньше 3 символов'.format(line_count))

    open_file.close()
        

except FileNotFoundError as exc:
    print(type(exc), 'Нет такого файла или директории')    
    
    
finally:
    print('общее число символов:', total_sym)
    
