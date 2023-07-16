names = ['Tom', 'Bob', 'Albert']
ages = [20, 45, 70]

people = zip(names, ages)
for i_person in people:
    print(i_person)             # кортежи 

print('\n', list(zip(names, ages)))   # список кортежей
print(dict(zip(names, ages)))   # словарь из 2х списков

print({i_names: i_ages + 10 
       for i_names, i_ages in zip(names, ages)})   # comprehansions + 10 years
