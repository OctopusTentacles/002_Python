# Recursive Generators

def permutations(items):
    if len(items) == 0: yield []
    else:
        for i in range(len(items)):
            for j in permutations(items[:i] + items[i+1:]):
                yield [items[i]] + j


for i in permutations(["r", "e", "d"]):
    print("".join(i))