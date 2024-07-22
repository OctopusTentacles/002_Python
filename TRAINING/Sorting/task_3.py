"""сравнение производительности пузырьковой и быстрой сортировок
"""


import time
import logging
import random

from typing import List


logger = logging.getLogger('sorting_time')

def bubble_sort(arr: List[int]) -> List[int]:
    logger.info('\tПузырьковая сортировка:')
    len_arr = len(arr)

    for i in range(len_arr):
        swapped = False

        for j in range(0, len_arr-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            logger.info(f'\tСортировка завершилась на {i-1} итерации.')
            break

    return arr


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    
    # Выбор опорного элемента (pivot):
    pivot = arr[len(arr) // 2]

    # Разделение массива:
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    # Рекурсивная сортировка и объединение:
    return quick_sort(left) + middle + quick_sort(right)
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # генерация случайного массива:
    array_size = 1000
    array = [random.randint(0, 1000) for _ in range(array_size)]
    logger.info(f'{array}')

    # копирование массива для каждой сортировки:
    copy_arr_for_bubble = array.copy()
    copy_arr_for_quick = array.copy()

    # измерение времени пузырьковой сортировки:
    start_time = time.time()
    arr_bubble_sort = bubble_sort(copy_arr_for_bubble)
    time_bubble_sort = time.time() - start_time
    logger.info(f'\tмассив отсортирован: {arr_bubble_sort}')
    logger.info(f'\tЗатраченное время {round(time_bubble_sort, 3)} сек.\n')

    # измерение времени быстрой сортировки:
    start_time = time.time()
    arr_quick_sort = quick_sort(copy_arr_for_quick)
    time_quick_sort = time.time() - start_time
    logger.info(f'\массив отсортирован: {arr_quick_sort}')
    logger.info(f'\tЗатраченное время {round(time_quick_sort, 3)} сек.\n')
