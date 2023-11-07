# Задача 4. Односвязный список
# Мы продолжаем тему структур данных и алгоритмов. 
# И в этот раз вам нужно реализовать односвязный список.

# Связный список — это структура данных, которая состоит из элементов, называющихся узлами. 
# В узлах хранятся данные, а между собой узлы соединены связями. 
# Связь — это ссылка на следующий или предыдущий элемент списка.

# В односвязном списке связь — это ссылка только на следующий элемент, 
# то есть в нём можно передвигаться только в сторону конца списка. 
# Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

# Реализуйте такую структуру данных без использования стандартных структур Python 
# (list, dict, tuple и прочие) и дополнительных модулей. Для структуры реализуйте следующие методы:

# append — добавление элемента в конец списка;
# get — получение элемента по индексу;
# remove — удаление элемента по индексу.
# Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

# Пример основной программы:

# my_list = LinkedList()
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print('Новый список:', my_list)
# Результат:

# Текущий список: [10 20 30]
# Получение третьего элемента: 30
# Удаление второго элемента.
# Новый список: [10 30]


class Node:
    """ class Node - создает новый узел, содержащий значение (value) 
                    и ссылку на следующий узел (next_node)
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    """ class LinkedList - связный список. 

        def __init__ -  при создании нового списка в поле head хранится
                        значение null, что означает, что список пустой.

        def append - принимает параметр value (значение). 
                    Создает новый узел, помещает туда значение 
                    и вставляет в конец списка.

        def get - 
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        list_link = []
        node = self.head
        while node.next_node:
            list_link.append(node.value)
            node = node.next_node
        list_link.append(node.value)
        return str(list_link)
            
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = Node(value)
    
    def get(self, index):
        count = 0
        node = self.head
        while count < index:
            node = node.next_node
            count += 1
        return node.value

    def remove(self, index):
        if index == 0:
            self.head = self.head.next_node
        else:
            count = 0
            node = self.head
            while count < index:
                pre_node = node
                node = node.next_node
                count += 1

            pre_node.next_node = node.next_node
            del node


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
