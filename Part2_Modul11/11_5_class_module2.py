# ПОДКЛЮЧАЕМЫЕ МОДУЛИ

# ОСНОВНОЙ СКРИПТ


# import garden
# чтобы избавиться от приписки garden.PotatoGarden(5)

# from garden import *
# но еще лучше вместо * указывать какие классы нам нужно импортировать

from garden import PotatoGarden

garden = PotatoGarden(5)

for _ in range(3):
    garden.grow_all()

garden.are_all_ripe()