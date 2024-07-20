# Реализуйте пузырьковую сортировку с выводом промежуточных шагов.


import logging

from typing import List


logger = logging.getLogger('Bubble_Sort')

def bubble_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)

    for i in range(len_arr):
        logger.info(f'\tИтерация {i+1}: массив {arr}')

        for j in range(0, len_arr-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        logger.info(f'\tперестановка с {j} на {j+1}')

    return arr



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Запуск пузырьковой сортировки')

    arr = [64, 34, 25, 12, 22, 11, 90, 5]
    logger.info(f'Текущий массив: {arr}')

    sorted_arr = bubble_sort(arr)
    logger.info(f'\tОтсортированный массив: {sorted_arr}')
