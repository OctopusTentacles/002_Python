# Задача 2. Документация API
# Обычно к открытым API прилагается подробная документация, где описывается 
# логика формирования ссылок и какие данные по ним можно получать (или отправлять!).

# Изучите документацию того же сайта по «Звёздным войнам».

# Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее. 
# А ещё попробуйте библиотеку swapi (о ней также в документации) и с её помощью 
# выведите начало сюжета из фильма «Новая надежда» (A New Hope).


import requests
import json


my_req = requests.get('https://swapi.dev/api/films/1/')
# print(my_req)
# Получаем <Response [200]> - запрос произведен успешно

# print(my_req.text)
if my_req.status_code == 200:
    json_dict = json.loads(my_req.text)     # десериализация JSON

    with open('my_test.json', 'w') as file:
        json.dump(json_dict, file, indent=4)    # сериализация JSON

    print(json_dict['opening_crawl'])