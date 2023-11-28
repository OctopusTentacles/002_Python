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


class LRU_Cache():
    pass


    @property
    def cache(self): # этот метод должен возвращать самый старый элемент
        
    @cache.setter
    def cache(self, new_elem): # этот метод должен добавлять новый элемент
