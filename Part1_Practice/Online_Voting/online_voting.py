""" Сервис онлайн-голосования. """






# Создать новое голосование.
# Функция для создания нового голосования____________________________
def create_voting():
    print('Голосование за автомобиль года.')

    count_models = int(input(
        'Сколько моделей авто участвуют в голосовании?: '
    ))

    # словарь для хранения моделей авто:
    models = dict()
    for i in range(count_models + 1):
        new_model = input(f'Введите модель {i}-го автомобиля: ')

        models.append(new_model)

        print('Голосование создано!')

        return models
    
# Проведение голосования.
# Функция для проведения голосования_________________________________
def conduct_voting(models):
    print('Выберите модель из списка:', ';'.join(models))
    print('Для подсчета голосов введите 0')

    # список для подсчета голосов на каждую модель,
    # список из 0 = длине models, [0, 0, 0]:
    votes = [0] * len(models)

    while True:
        choice = input('Ваш выбор?:')
        if choice == 0:
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

    print("Голосование завершено!")

    max_votes = max(votes)
    winner_index = votes.index(max_votes)
    print("Лучший автомобиль года:", models[winner_index])
    print("Количество голосов:", max_votes)

