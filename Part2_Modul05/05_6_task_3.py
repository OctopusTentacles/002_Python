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

symbols = '@№$%^&\*()'
extension = '.txt .docx'

print(symbols)
print(extension)

name_file = input('Название файла: ')

for index in range(len(symbols)):
    if name_file.startswith(symbols[index]):
        print('Ошибка: название начинается на один из специальных символов.')
        break
for index in range(len(extension)):
    if name_file.endswith(extension[index]):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
        break
else:
    print('Файл назван верно.')
    
    
# if name_file.startswith([i for i in len(name_file)]):
#     print('Ошибка: название начинается на один из специальных символов.')
# elif name_file.endswith(extension):
#     print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
# else:
#     print('Файл назван верно.')
