# Задача 3. Файлы

# В одной IT-компании существует негласный закон об именовании текстовых 
# документов:

# Название файла не должно начинаться на один из специальных символов: @№$%^&\*().
# Файл заканчивается расширением .txt или .docx.
# Напишите программу, которая получает на вход полное название файла и 
# проверяет его по этим правилам.

# Пример 1:
# Название файла: @example.txt
# Ошибка: название начинается на один из специальных символов.

# Пример 2:
# Название файла: example.ttx
# Ошибка: неверное расширение файла. Ожидалось .txt или .docx.

# Пример 3:
# Название файла: example.txt
# Файл назван верно.


def begining(text, symbol):
    for i in range(len(symbol)):
        if text.startswith(symbol[i]):
            return True
        
def ending(text, extension):
     for i in range(len(extension)):
        if text.endswith(extension[i]):
            return True


symbols = '@№$%^&\*()'
extension = '.txt .docx'

symbols_list = list(symbols)
extension_list = (extension).split(' ')

print(symbols_list)
print(extension_list)

name_file = input('Название файла: ')

if begining(name_file, symbols_list):
    print('Ошибка: название начинается на один из специальных символов')

elif ending(name_file, extension_list):    
    print('Файл назван верно.')

else:       
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    
# ну в общем не знаю...
# целый день пытался что-то придумать через join, split, list comprehension - 
# ничего не получалось. Уже вечером, от безисходности, решил все расписать - 
# вроде получилось - все работает.
# но есть вопрос: почему символ \ в списке становится \\, но определяется как \ ?

