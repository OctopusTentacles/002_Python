def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
for i in f:
    print(i, end=" ")
print()


def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()

count = 0
for i in f:
    print(i, end=" ")
    count += 1
    if count > 10:
        break