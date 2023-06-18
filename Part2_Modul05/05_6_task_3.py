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

symbols = list('@№$%^&\*()')
extension = '.txt .docx'.split()

print(symbols)
print(extension)

name_file = input('Название файла: ')

if name_file.startswith(symbols):
    print('Ошибка: название начинается на один из специальных символов.')