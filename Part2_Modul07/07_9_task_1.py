# Задача 1. Ревью кода

# Ваня работает middle-разработчиком на Python в IT-компании. 
# Один кандидат на позицию junior-разработчика прислал ему код тестового задания.

# В задании был словарь из трёх студентов. Необходимо:
# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: 
# полный список интересов всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде вызывается функция, значения присваиваются отдельным переменным 
# и выводятся на экран.

# Ваня — очень придирчивый программист, и после просмотра кода он понял, что этого 
# кандидата на работу не возьмёт, хотя он выдаёт верный результат. Вот код кандидата:

# Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться 
# (только если очень захочется). Убедитесь, что программа верно работает 
# Проверки на существование записей в словаре не обязательны, но приветствуются.

# Результат работы программы:

# Список пар "ID студента — возраст": [(1, 23), (2, 24), (3, 22)]
# Полный список интересов всех студентов: {'running', 'computer games', 'math', 'languages', 
#                                          'biology, swimming', 'health food'}
# Общая длина всех фамилий студентов: 20

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def collect_from_dict_1(search):
    collection = []
    for key in students.values():
        for value in key[search]:
            collection.append(value)
    return collection


ID_ages = [(key, value['age']) for key, value in students.items()]
print('Список пар "ID студента — возраст":', ID_ages)

interests = collect_from_dict_1('interests')
print('Полный список интересов всех студентов:', interests)

length_surnames = collect_from_dict_1('surname')
print('Общая длина всех фамилий студентов:', len(length_surnames))

# ___________________________________________________________________________

print('\nвариант - 2')

def collect_from_dict_2(data):
    if not data:
        return print('словарь пуст')
    collection_interest = []
    collection_surname = 0
    for value in data.values():
        collection_interest.append(value['interests'])
        collection_surname += len(value['surname'])
    return collection_interest, collection_surname

ID_ages = [(key, value['age']) for key, value in students.items()]
print('\nСписок пар "ID студента — возраст":', ID_ages)

interests, length_surnames = collect_from_dict_2(students)

print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', length_surnames)
