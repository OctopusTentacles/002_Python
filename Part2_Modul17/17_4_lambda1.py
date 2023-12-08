# Задача 1. Минимум и максимум
# Мы знаем, что для нахождения минимального и максимального значений в наборе 
# данных можно использовать две встроенные функции: min() и max(). 
# И у них тоже можно использовать именованный аргумент key. 

# Скажем, дан вот такой список, в котором хранятся результаты 
# соревнований в виде словарей:


from typing import List


grades: List[Dict[str, Union[str, int]]] = [
{'name': 'Kenneth', 'score': 3}, 
{'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24}, 
{'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, 
{'name': 'Jana', 'score': 45}, {'name': 'Sarah', 'score': 90}, 
{'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
{'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, 
{'name': 'Richard', 'score': 78}, {'name': 'Warren', 'score': 7}, 
{'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
{'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, 
{'name': 'James', 'score': 54},{'name': 'Annie', 'score': 87}, 
{'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
{'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, 
{'name': 'Aaron', 'score': 3},{'name': 'Ronnie', 'score': 47}, 
{'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},

]
# Напишите код, который выводит на экран минимальное и максимальное количество 
# очков из этого списка. Используйте только встроенные функции и лямбда-функции, 
# то есть реализуйте решение «в две строки».





# ============================================
# def string_to_int(elem: str) -> int:
#     return int(elem[4:])


users: List[str] = ['user1', 'user20', 'user3', 'user22', 'user100']
# sorted_users = sorted(users, key=string_to_int)
sorted_users = sorted(users, key=lambda elem: int(elem[4:]))

print(sorted_users)

x = lambda a: a + 10
print(x(5))