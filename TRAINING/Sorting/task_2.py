"""
    Обратный порядок: Попробуйте отсортировать массив 
    в обратном порядке (от большего к меньшему) 
    с помощью пузырьковой сортировки.
"""


import logging

from typing import List


logger = logging.getLogger('revers_bubble_sort')

def revers_bubble_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)

    for i in range(len_arr):
        swapped = False
        logger.info(f'\tИтерация {i}')

        for j in range(0, len_arr-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                logger.info(f'\tСортировка {arr}')
        if not swapped:
            logger.info(f'\tСортировка завершилась на {i-1} итерации.')
            break
    
    return arr


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info(f'\tЗапуск обратной сортировки:')

    arr = [64, 34, 25, 12, 22, 11, 90, 5]
    logger.info(f'\tТекущий массив {arr}')

    sorted_arr = revers_bubble_sort(arr)
    logger.info(f'\tМассив отсортирован {sorted_arr}')