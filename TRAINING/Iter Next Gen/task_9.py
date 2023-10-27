# Recursive Generators

def permutations(items):
    if len(items) == 0: yield []


for i in permutations(["r", "e, "d]):
    print("".join(i))