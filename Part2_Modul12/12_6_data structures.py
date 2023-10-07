"""
12.6 Готовые реализации структур данных: очередь, стек, бинарное дерево

Модуль collections
Наиболее популярные и полезные структуры данных модуля
1. deque
"""
from collections import deque
queue = deque()
queue.append(1) # Добавление элемента в конец очереди
queue.append(2)
queue.appendleft(3) # Добавление элемента в начало очереди

print(queue) # Вывод: deque([3, 1, 2])

item = queue.popleft() # Удаление и получение элемента из начала очереди
print(item) # Вывод: 3