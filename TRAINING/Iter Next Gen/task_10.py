# A Generator of Generators

def firstn(generator, n):
    g = generator()
    for i in range(n):
        yield next(g)

def fibonacci():
    """ A Fibonacci number generator """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b 

print(list(firstn(fibonacci, 10)))