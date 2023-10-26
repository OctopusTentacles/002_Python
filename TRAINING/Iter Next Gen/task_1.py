
cities = ["Berlin", "Vienna", "Zurich"]
iterator_obj = iter(cities)
print(iterator_obj)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


class Reverse:
    """
        Creates Iterators for looping over a sequence backwards.
    """
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.length -= 1
        return self.data[self.length]


lst = [34, 978, 42]
rev_lst = Reverse(lst)
for elem in rev_lst:
    print(elem, end=' ')