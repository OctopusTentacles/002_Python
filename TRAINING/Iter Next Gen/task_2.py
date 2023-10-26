class Cycle(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter_obj = iter(iterable)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                next_obj = next(self.iter_obj)
                return next_obj
            except StopIteration:
                self.iter_obj = iter(self.iterable)


x = Cycle("abc")

for i in range(10):
    print(next(x), end=", ")