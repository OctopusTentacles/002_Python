def count(value = 0, step=1):

    while True:
        yield value
        value += step


counter = count()     # count will start with 0
for i in range(10):
    print(next(counter), end=", ")


start_value = 2.1
step_value = 0.3
print("\nNew counter")

counter = count(start_value, step_value)
for i in range(10):
    print(f"{next(counter):.2f}", end=", ")
