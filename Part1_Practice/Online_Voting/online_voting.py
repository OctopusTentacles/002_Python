""" Сервис онлайн-голосования. """


# Создать новое голосование.
# Функция для создания нового голосования____________________________
def create_voting():
    print('\nГолосование за автомобиль года.\n')

    count_models = int(input(
        'Сколько моделей авто участвуют в голосовании?: '
    ))

    # словарь для хранения моделей авто:
    models = list()
    for i in range(1, count_models + 1):
        new_model = input(f'Введите модель {i}-го автомобиля: ')

        models.append(new_model)

    print('\nГолосование создано!')

    return models
    
# Проведение голосования.
# Функция для проведения голосования_________________________________
def conduct_voting(models):
    print('Выберите модель из списка:', '; '.join(models))
    print('Для подсчета голосов введите 0\n')

    # список для подсчета голосов на каждую модель,
    # список из 0 = длине models, [0, 0, 0]:
    votes = [0] * len(models)

    while True:
        choice = input('\nВаш выбор?: ')
        if choice == '0':
            break
        elif choice in models:
            index = models.index(choice)
            votes[index] += 1
            print('Ваш голос принят!')
        else:
            print('Выберите модель из списка!')

    return votes

# Получить результат голосования.____________________________________
def calculate_results(models, votes):
    '''Функция остановки голосования и получения результата. '''

    print('\nГолосование завершено!')

    max_votes = max(votes)
    winner_index = votes.index(max_votes)
    print('Лучший автомобиль года:', models[winner_index])
    print('Количество голосов:', max_votes)


# MAIN===============================================================
def main():
    models = create_voting()
    votes = conduct_voting(models)
    calculate_results(models, votes)


# Запуск программы:__________________________________________________
main()