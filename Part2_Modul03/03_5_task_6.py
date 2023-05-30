# Задача 6. Ролики

# Частная контора даёт в прокат ролики самых разных размеров. 
# Человек может надеть ролики только своего размера.

# Пользователь вводит два списка размеров: 
# N размеров коньков и K размеров ног людей. 
# Реализуйте код, который определяет, какое наибольшее число 
# человек может одновременно взять ролики и пойти кататься.

# Не забывайте, что один человек может надеть только одну пару роликов! 
# (и наоборот - одну пару роликов может надеть только один человек!)

# Пример:
# Кол-во коньков: 4
# Размер 1-й пары: 41
# Размер 2-й пары: 40
# Размер 3-й пары: 39
# Размер 4-й пары: 42

# Кол-во людей: 3
# Размер ноги 1-го человека: 42
# Размер ноги 2-го человека: 41
# Размер ноги 3-го человека: 42

# Наибольшее кол-во людей, которые могут взять ролики: 2


def bubble_sort(my_list):
    for index in range(len(my_list) - 1):
        for i in range(len(my_list) - index - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


skates_list = []
people_list = []

skates = int(input('Кол-во коньков: '))
for skate in range(1, skates + 1):
    print(f'Размер {skate} пары: ', end='')
    skates_list.append(input())


people = int(input('\nКол-во людей: '))
for i_size in range(1, people + 1):
    print(f'Размер ноги {i_size}-го человека: ', end='')
    people_list.append(input())

people_list.extend(skates_list)
bubble_sort(people_list)

men = 0
for i_man in range(people_list):
    if people_list[i_man] == people_list[i_man + 1]:
        men += 1
        people_list.remove(i_man, i_man + 1)


print('ноги', people_list)
