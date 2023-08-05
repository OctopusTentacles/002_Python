# Задача 2. Поиск элемента — 2
# Что нужно сделать
# Пользователь вводит искомый ключ. Если он хочет, то может ввести 
# максимальную глубину — уровень, до которого будет просматриваться структура. 

# Напишите функцию, которая находит заданный пользователем 
# ключ в словаре и выдаёт значение этого ключа на экран. 
# По умолчанию уровень не задан. В качестве примера можно 
# использовать такой словарь:

# Пример 1
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}

# Пример 2
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None


def search_element(data, tag, deep_value=None):

    if tag in data:
        return data[tag]
    
    if deep_value > 1:
        for value in data.values():
            if isinstance(value, dict):
                result = search_element(value, tag, deep_value - 1)
                if result:
                    break
    else:
        return result



site = {'html': {
                'head': {'title': 'Мой сайт'}, 
                'body': {'h2': 'Здесь будет мой заголовок', 
                        'div': 'Тут, наверное, какой-то блок', 
                        'p': 'А вот здесь новый абзац'
                        }
                }
        }

search_key = input('Введите искомый ключ: ')
deep = input('Хотите ввести максимальную глубину? Y/N: ').title()
if deep == 'Y':
    deep_value = int(input('Введите максимальную глубину: '))
    value = search_element(site, search_key, deep_value)
else:
    value = search_element(site, search_key)

print('Значение ключа:', value)
