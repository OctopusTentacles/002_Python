# yield from

def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i


g1 = gen1()
print("g1: ", end="")
for i in g1:
    print(i, end=" ")

# ====================================

def gen2():
    yield from "Python"
    yield from range(5)

g2 = gen2()
print("\ng2: ", end="")
for i in g2:
    print(i, end=" ")