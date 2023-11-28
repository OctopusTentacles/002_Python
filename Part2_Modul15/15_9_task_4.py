# Задача 4. Кэширование запросов
# Контекст 
# Вы разрабатываете программу для кэширования запросов к внешнему API. 
# Часто повторяющиеся запросы занимают много времени, поэтому вы решаете создать 
# класс LRU Cache (Least Recently Used Cache), который будет хранить ограниченное 
# количество запросов и автоматически удалять самые старые при достижении лимита. 
# Это позволит значительно ускорить повторяющиеся запросы, 
# так как данные будут браться из кэша, а не отправляться повторно.

# Задача
# Создайте класс LRU Cache, который хранит ограниченное количество объектов и, 
# при превышении лимита, удаляет самые давние (самые старые) использованные элементы. 
# Реализуйте методы добавления и извлечения элементов с использованием декораторов 
# property и setter.


# Советы
# Не забывайте обновлять порядок использованных элементов. 
# В итоге должны удаляться давно использованные элементы, а не давно добавленные, 
# так как давно добавленный элемент может быть популярен, и его удаление не поможет 
# ускорить новые запросы.


class LRUCache:

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.__cache = dict()


    @property
    def cache(self): 
        """Возвращает самый старый элемент
        """
        if len(self.__cache) > 0:
            return next(iter(self.__cache.items()))
        # else: return None

    @cache.setter
    def cache(self, new_elem: tuple): 
        """этот метод должен добавлять новый элемент
        """
        key, value = new_elem
        self.__cache[key] = value

    def get(self, key: str):
        value = self.__cache[key]
        return value


    def print_cache(self):
        for key, value in self.__cache.items():
            print(f"{key} : {value}")


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# # Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2")) # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4