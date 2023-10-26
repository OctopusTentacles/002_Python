# Using a 'return' in a Generator

def gen():
    yield 1
    raise StopIteration(42)
    yield 2 


g = gen()
print(next(g))
# print(next(g))
# print(next(g))

def gen():
    yield 1
    return 42
    yield 2 


g = gen()
print(next(g))
print(next(g))
print(next(g))