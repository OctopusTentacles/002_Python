# Задача 3. Гистограмма частоты
# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих 
# данных будет строиться гистограмма частоты букв. 

# Напишите программу, которая получает сам текст и считает, 
# сколько раз в строке встречается каждый символ. На экран нужно вывести 
# содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное 
# значение частоты.

# Пример:
# Введите текст: Здесь что-то написано
#   : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1
# Максимальная частота: 3

def histogram(string):

    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict



text = input('Введите текст: ')
hist = histogram(text)

for i in sorted(hist.keys()):
    print(i, ':', hist[i])
print('Максимальная частота: ', max(hist.values()))