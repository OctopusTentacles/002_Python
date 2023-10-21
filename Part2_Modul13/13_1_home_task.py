# Задача 5. Стек
# Module 12_7_task_5.py

class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return str(self.__st)
    
    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()