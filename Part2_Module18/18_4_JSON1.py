# Задача 1. Звёздные войны
# Повторите пример парсинга, разобранный в уроке: перейдите на сайт с API, 
# посвящённый вселенной Star Wars.

# После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).

# Затем напишите программу, которая парсит данные об этом человеке, изменяет его имя 
# на ваше собственное и сохраняет результат в виде JSON-файла.

# Дополнительно: обратите внимание на значение ключа homeworld — там также 
# хранится ссылка. В том же коде спарсите эту ссылку и посмотрите, что там. 

# Примечание: API тоже пишут люди, а значит, время от времени его могут как-то 
# менять и усовершенствовать, поэтому будьте внимательны: 
# может быть, ссылка уже хранится в другом ключе.


import requests     # pip install requests
import json


# my_req = requests.get("https://www.google.com/")
# print(my_req)
# Response [200] - запрос произведен успешно, результат получен [статус]
# print(my_req.text)

# JSON (JavaScript Object Notation) - текстовый формат обмена данными.
    # набор пар ключ-значение (словарь, хэш-таблица)
    # либо упорядоченный набор значений (список)

my_req = requests.get('https://swapi.dev/api/people/3/')    # parsing
print(my_req.text)

data = json.loads(my_req.text)  # десериализация JSON
print(data)

data["name"] = 'R10-D10'
print(data['name'])

with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4)   # сериализация JSON

with open('my_test.json', 'r') as file:
    data = json.load(file)

print(data)
