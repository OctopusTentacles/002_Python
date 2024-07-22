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






if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)