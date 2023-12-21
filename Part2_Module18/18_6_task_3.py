# Задача 3. May the force be with you
# Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. 
# Ссылка на документацию: Documentation.

# Внимательно изучите документацию этого API и напишите программу, 
# которая выводит на экран (и в JSON-файл) информацию о пилотах 
# легендарного корабля Millennium Falcon.

# Информация о корабле должна содержать следующие пункты:
# название,
# максимальная скорость,
# класс,
# список пилотов.

# Внутри списка о каждом пилоте должна быть следующая информация:
# имя,
# рост,
# вес,
# родная планета,
# ссылка на информацию о родной планете.


import os
import json
import requests
from typing import Dict, Any

# чтобы созданный файл был в одно каталоге:
cur_dir = os.path.dirname(__file__)
cache_dict = dict()

def api_info(url: str, name: str) -> Dict[str, Any]:
    """ функция для поиска информации по ресурсу API.
        param url: ссылка на ресурс API.
        param name: имя того что нас интересует.
    """

    # запрос:
    response = requests.get(url)
    if response.status_code == 200:
        # десериализация JSON:
        ship_data = json.loads(response.text)

        # все данные лежат в ключе results:
        for result in ship_data['results']:
            if result["name"] == name:
                starship_info = {
                    "название": result["name"], 
                    "максимальная скорость": result["max_atmosphering_speed"],
                    "класс": result["starship_class"],
                    "список пилотов": []                    
                }

                # список пилотов содержит ссылки:
                for url_pilot in result["pilots"]:

                    if url_pilot not in cache_dict:
                        request_pilot = requests.get(url_pilot)
                        if request_pilot.status_code == 200:
                            
                            # десериализация JSON:
                            pilot_data = json.loads(request_pilot.text)
                            cache_dict[url_pilot] = pilot_data
                    else:
                        pilot_data = cache_dict[url_pilot]
                    # словарь на каждого пилота:
                    pilot_info = {
                        "имя": pilot_data["name"],
                        "рост": pilot_data["height"],
                        "вес": pilot_data["mass"],
                        "родная планета": "",
                        "ссылка на информацию о родной планете": pilot_data["homeworld"]
                    }

                    # родная планета - ссылка, а нам нужно имя -> str:
                    request_planet = requests.get(pilot_data["homeworld"])
                    if request_planet.status_code == 200:
                        # десериализация JSON:
                        planet_data = json.loads(request_planet.text)
                        pilot_info["родная планета"] = planet_data["name"]

                        # добавляем в список пилотов словарь на каждого пилота:
                        starship_info["список пилотов"].append(pilot_info)
        return starship_info
    

# MAIN===================================================================================
my_url = "https://swapi.dev/api/starships/"
search_name = "Millennium Falcon"

starship = api_info(my_url, search_name)

# сериализация JSON и запись в файл:
with open(os.path.join(cur_dir, "info.json"), "w", encoding='utf-8') as file:
    json.dump(starship, file, indent=4, ensure_ascii=False)

    # вывод в консоль в JSON формате:
    print(json.dumps(starship, indent=4, ensure_ascii=False))
