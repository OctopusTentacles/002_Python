names = ['Tom', 'Bob', 'Albert']
ages = [20, 45, 70]

people = zip(names, ages)
for i_person in people:
    print(i_person)             # кортежи 

print(list(zip(names, ages)))   # список кортежей