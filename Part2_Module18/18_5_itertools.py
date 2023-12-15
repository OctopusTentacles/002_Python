# itertools


import itertools


colors = ['red', 'blue', 'green', 'yellow']
for item in itertools.permutations(colors, 2):
    print(item)

print('=' * 50)

for item in itertools.combinations(colors, 2):
    print(item)