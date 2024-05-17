""" Сервис онлайн-голосования. """







# MAIN MENU============================================================
def main():
    print('Голосование за автомобиль года.')

    count_models = int(input(
        'Сколько моделей авто участвуют в голосовании?: '
    ))

    # словарь для хранения моделей авто:
    car_models = dict()
    for i in range(count_models + 1):
        new_model = input(f'Введите модель {i}-го автомобиля: ')

        car_models.append(new_model)

        print('Голосование создано!')

        return car_models