# Реализуйте пузырьковую сортировку с выводом промежуточных шагов.


import logging

from typing import List


logger = logging.getLogger('Bubble_Sort')

def bubble_sort(arr: List[int]) -> List[int]:
    ...



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Запуск пузырьковой сортировки')

    arr = [64, 34, 25, 12, 22, 11, 90]
    logger.info(f'Текущий массив: {arr}')

    sorted_arr = bubble_sort(arr)
    logger.info(f'Отсортированный массив: {sorted_arr}')
