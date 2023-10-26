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