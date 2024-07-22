"""сравнение производительности пузырьковой и быстрой сортировок
"""


import time
import logging
import random

from typing import List


logger = logging.getLogger('sorting_time')

def bubble_sort(arr: List[int]) -> List[int]:
    len_arr = len(arr)

    for i in range(len_arr):
        swapped = False

        for j in range(0, len_arr-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not swapped:
            logger.info(f'\tСортировка завершилась на {i-1} итерации.')
            break

    return arr

def quick_sort(arr: List[int]) -> List[int]:





if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # генерация случайного массива:
    array_size = 1000
    array = [random.randint(0, 1000) for _ in range(array_size)]

    # копирование массива для каждой сортировки:
    copy_arr_for_bubble = array.copy()
    copy_arr_for_quick = array.copy()

    # измерение времени пузырьковой сортировки:
    start_time = time.time()
    arr_bubble_sort = bubble_sort(copy_arr_for_bubble)
    time_bubble_sort = time.time() - start_time
    logger.info(f'\tПузырьковая сортировка: {arr_bubble_sort}')
    logger.info(f'\tЗатраченное время {time_bubble_sort}')
