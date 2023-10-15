# Задача 5. Стек
# Что нужно сделать
# Мы уже говорили, что в программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых структур является стек. 

# Стек — это абстрактный тип данных, представляющий собой список элементов, 
# организованных по принципу LIFO (англ. last in — first out, 
#                                  «последним пришёл — первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой видна, 
# является самая верхняя. Чтобы получить доступ, например, к третьей снизу книге, 
# нам нужно убрать все книги, лежащие сверху, одну за другой.

# Напишите класс, который реализует стек и его возможности 
# (достаточно будет добавления и удаления элемента). 

# После этого напишите ещё один класс — «Менеджер задач». 
# В менеджере задач можно выполнить команду «новая задача», в которую 
# передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе 
# стека (не наследование). При выводе менеджера в консоль все задачи должны быть 
# отсортированы по следующему приоритету: чем меньше число, тем выше задача.

# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)

# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду

# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.


class MyStack():
    def __init__(self):
        self.stack = list()
    
    def put(self, item):
        self.stack.insert(0, item)

    def get(self):
        print("Верхний элемент", end=" ")
        return self.stack[0]
    
    def delete(self):
        if len(self.stack) == 0:
            return "Стек пуст"
        else:
            print("Удаляем верхний элемент", end=" ")
            return self.stack.pop(0)

    def __str__(self):
        return f"Стек = {str(self.stack)}"
    
class TaskManager():
    def __init__(self):
        self.my_task = MyStack()
        self.get_task = dict()

    def new_task(self, task, priority):
        self.get_task[priority] = task
        self.my_task.put(self.get_task())
        

    
# my_list = MyStack()

# one = {"сделать уборку", 4}
# two = {"отдохнуть", 1}
# three = {"поесть", 2}

# my_list.put(one)
# my_list.put(two)
# my_list.put(three)
# print(my_list)

# print(my_list.get())
# print(my_list)
# print(my_list.delete())
# print(my_list)
# print(my_list.delete())
# print(my_list)
# print(my_list.delete())
# print(my_list)
