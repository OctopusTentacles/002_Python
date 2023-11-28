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

    def __init__(self, capacity: int) -> None:
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
    def cache(self, new_elem: tuple) -> None: 
        """ Добавляет новый элемент в кэш.
            :param new_elem: Кортеж (ключ, значение) нового элемента.
        """

        key, value = new_elem
        # удалить самый старый элемент, если превышен лимит:
        if len(self.__cache) >= self.capacity:
            old_elem = next(iter(self.__cache))
            del self.__cache[old_elem]
        # добавить новый элемент в кэш:
        self.__cache[key] = value

    def get(self, key: str) -> str:
        """
            Возвращает значение по ключу и обновляет порядок элементов в кэше.

            :param key: Ключ элемента.
            :return: Значение элемента по ключу.
        """
        # самый старый 1, потом 3, самый новый 2
        value = self.__cache[key]
        return value


    def print_cache(self):
        """ Выводит текущий кэш в консоль."""

        print("LRU Cache:")
        for key, value in self.__cache.items():
            print(f"{key} : {value}")


# MAIN==============================================================================
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