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


# 1 ===========================================================================
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
                
    def __repr__(self):
        """def __repr__ - возвращает более информативное (официальное) 
                          строковое представление объекта
        """
        return str(self.stack)
    

class TaskManager():
    def __init__(self):
        self.my_tasks = MyStack()        

    def new_task(self, task, priority):
        self.get_task = MyStack()
        self.get_task.put(task)
        self.get_task.put(priority)

        self.my_tasks.put(self.get_task)
        # print("Получаем стек:", self.my_tasks)

    def sort(self, data):
        self.my_tasks.quick_sort(data)

    def __repr__(self) -> str:
        return str(self.my_tasks)
        

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print("\n1. Получаем стек:", manager)

# стэк получается, но я не могу придумать как отсортировать 
# TypeError: 'TaskManager' object is not subscriptable
#==============================================================================

# 2 ===========================================================================
class TaskManager():
    def __init__(self):
        self.my_tasks = [] 

    def new_task(self, task, priority):
        self.get_task = []
        self.get_task.insert(0, task)
        self.get_task.insert(0, priority)

        self.my_tasks.insert(0, self.get_task)

    def sorting(self):
        for index, item_1 in enumerate(self.my_tasks):
            for item_2 in self.my_tasks[index+1:]:
                if item_1[0] == item_2[0]:
                    item_1.append(item_2[1])
                    self.my_tasks.pop(index+1)

        sorting = sorted(self.my_tasks)
        for index in sorting:
            if len(index) == 3:
                print("{0} - {1}; {2}".format(index[0], index[1], index[2]))
            elif len(index) == 2:
                print("{0} - {1}".format(index[0], index[1]))
        return sorted(sorting)
    
    def __repr__(self) -> str:
        return str(self.my_tasks)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print("\n2. Получаем Стэк:", manager, "\n")

print("2. Сортированный Стэк:",manager.sorting())

# тут отсортировал, вывел как в примере, но без class MyStack
#==============================================================================
