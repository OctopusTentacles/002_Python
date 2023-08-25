import os

cur_dir = os.path.dirname(__file__)
line_count = 0
total_sym = 0
    
try:
    with open(os.path.join(cur_dir, 'people.txt'), 'r', encoding='utf8') as people_file:
    # open_file = open(os.path.join(cur_dir, 'people.txt'), 'r', encoding='utf8')
    
        for i_line in people_file.readlines():
            line_count += 1
            sym_in_line = 0
            for i_sym in i_line:
                if i_sym.isalpha():
                    sym_in_line += 1
                    total_sym += 1
            print('в строке', sym_in_line, 'символов')
                
            if sym_in_line < 3:
                raise BaseException('Длина {} строки меньше 3 символов'.format(line_count))

    # open_file.close()
        
except FileNotFoundError as exc:
    print(type(exc), 'Нет такого файла или директории')    
    
finally:
    print('общее число символов:', total_sym)
    print(people_file.closed)