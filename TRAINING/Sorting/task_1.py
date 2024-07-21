# Реализуйте пузырьковую сортировку с выводом промежуточных шагов.


import logging

from typing import List


logger = logging.getLogger('Bubble_Sort')

def bubble_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)
    
    # Внешний цикл по всем элементам массива
    for i in range(len_arr):
        logger.info(f'\tИтерация {i+1}: массив {arr}')

        # флаг, который отслеживает, были ли сделаны перестановки 
        # на текущей итерации. 
        swapped = False

        # Внутренний цикл, который проходит по неотсортированной части массива
        for j in range(0, len_arr-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если нет перестановок, массив уже отсортирован, 
        # и можно завершить выполнение раньше.
        if not swapped:
            break

        logger.info(f'\tперестановка: {arr}')

    return arr


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('\tЗапуск пузырьковой сортировки')

    arr = [64, 34, 25, 12, 22, 11, 90, 5]
    logger.info(f'\tТекущий массив: {arr}')

    sorted_arr = bubble_sort(arr)
    logger.info(f'\tОтсортированный массив: {sorted_arr}')
