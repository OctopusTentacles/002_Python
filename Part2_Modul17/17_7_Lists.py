# Списки и их сортировка

# Списки в Python — это упорядоченные изменяемые коллекции объектов. 
# Они могут содержать данные разных типов, таких как числа, строки, списки.
# Списки в Python — мощный инструмент для работы с упорядоченными коллекциями данных, 
# а их гибкость используется во множестве сценариев программирования.

# Особенности и применение списков

# Списки в Python имеют следующие особенности: 
# Упорядоченность. Элементы списка хранятся в определённом порядке, 
# этот порядок сохраняется при выполнении операций над списком.

# Изменяемость. Списки могут быть изменены после создания. Это означает, что вы можете 
# добавлять, удалять и изменять элементы списка.

# Гибкость. Списки могут содержать элементы различных типов данных, и вы можете 
# комбинировать элементы в любом порядке и количестве.

# Списки используют: 

# Для хранения и обработки данных. Списки стоит выбрать для хранения данных, 
# если вам при хранении нужно будет изменять данные и сохранять порядок элементов.

# Для реализации стека и очереди. 

# Для работы с алгоритмами и структурами данных. Списки — основной инструмент для 
# реализации и использования различных алгоритмов и структур данных, включая 
# сортировку, поиск, объединение и другие операции.

# =======================================================================================

# Стандартный алгоритм сортировки.

# В стандартной библиотеке Python есть готовая реализация алгоритма сортировки для списков. 
# Она используется в функции sorted() и методе list.sort(). Начиная с Python 2.3 
# стандартным алгоритмом для сортировки был выбран Timsort, 
# его разработал Тим Петерс (Tim Peters).

# Timsort — гибридный алгоритм, который комбинирует идеи из сортировки слиянием (merge sort) 
# и сортировки вставками (insertion sort) для достижения эффективности в разных сценариях 
# сортировки, при этом он сохраняет относительный порядок равных элементов.

Timsort:
# адаптивный алгоритм, который оптимизирован для разных случаев, 
# включая частично отсортированные или обратно отсортированные списки. 
# Он эффективно обрабатывает списки с повторяющимися элементами.

# Реализация алгоритма Timsort в Python скрыта от пользователя. 
# Вам не требуется заботиться о деталях реализации, можно просто использовать функцию 
# sorted() или метод list.sort() для сортировки списков в Python, а библиотека сама 
# позаботится о выборе подходящего алгоритма сортировки в зависимости от данных и 
# сценария использования.
# Это не значит, что нужно полностью доверить всё функции sorted() и методу list.sort(). 
# Знание разных алгоритмов сортировки списков всё ещё важно для программиста.

# Когда стандартная сортировка неэффективна
# Хотя стандартная сортировка Timsort обычно обладает хорошей производительностью и 
# обеспечивает стабильность, иногда другие алгоритмы сортировки могут подойти лучше.
# Сортировка в обратном порядке. 
# Если вам требуется отсортировать список в обратном порядке, использование стандартной 
# сортировки в Python может быть неэффективным. Лучше использовать алгоритм сортировки, 
# специально разработанный для сортировки в обратном порядке, например сортировку 
# пузырьком (bubble sort) в обратном порядке.
# Сортировка частично отсортированных списков. 
# Когда список уже частично отсортирован, стандартная сортировка Timsort может 
# потребовать дополнительных ресурсов и времени на выполнение сравнений и перемещений 
# элементов. В таких ситуациях алгоритмы, оптимизированные для почти отсортированных 
# списков, такие как сортировка вставками (insertion sort) или сортировка выбором 
# (selection sort), могут быть более эффективными.
# Ограниченные ресурсы. 
# Если ваши ресурсы ограниченны (например, память), но вам нужно сортировать большие 
# объёмы данных, стандартная сортировка Timsort может быть не самым оптимальным выбором. 
# Можно рассмотреть алгоритмы сортировки, требующие меньше дополнительной памяти, 
# например внешнюю сортировку слиянием (external merge sort) или карманную/корзинную 
# сортировку (bucket sort).

# =======================================================================================

# bubble sort
# Сортировка пузырьком (bubble sort) — это простой алгоритм сортировки, который проходит 
# по списку несколько раз, сравнивая пары соседних элементов и меняя их местами, 
# если они находятся в неправильном порядке. Этот процесс повторяется до тех пор, 
# пока весь список не будет отсортирован.

# Преимущества сортировки пузырьком
# Простота реализации. Этот алгоритм легко понять и реализовать. 
# Он требует только базовых операций сравнения и обмена элементов.
# Понятность. Сортировка пузырьком имеет простую и интуитивно понятную идею. 
# Каждая итерация алгоритма продвигает наибольший элемент в конец списка, поэтому 
# процесс сортировки напоминает всплытие пузырька воды.

# Недостатки сортировки пузырьком
# Низкая производительность. Временна́я сложность сортировки пузырьком составляет 
# O(n^2), где n — количество элементов в списке. Это делает её неэффективной для 
# сортировки больших объёмов данных.
# Неэффективность. Алгоритм сортировки пузырьком часто требует множественных 
# проходов по списку. Это делает его неэффективным для случаев, когда список уже 
# частично отсортирован или содержит небольшое количество неотсортированных элементов.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Сравниваем пару соседних элементов
             if lst[j] > lst[j + 1]:
                # Если элементы находятся в неправильном порядке, меняем их местами
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
# Пример использования
numbers = [5, 3, 8, 2, 1]
bubble_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]

# =======================================================================================

# insertion sort
# Сортировка вставками (insertion sort) — это простой алгоритм сортировки, 
# который постепенно строит отсортированную последовательность, один элемент за другим, 
# вставляя каждый новый элемент в правильное место.

# Преимущества сортировки вставками
# Простота реализации. Сортировка вставками — один из наиболее простых алгоритмов 
# сортировки для понимания и реализации. Она требует только базовых операций сравнения 
# и перестановки элементов.
# Эффективность для малых размеров. Для небольших списков или уже частично упорядоченных 
# данных сортировка вставками может быть эффективнее, чем другие алгоритмы сортировки, 
# такие как сортировка слиянием или быстрая сортировка. Она имеет низкую структурную 
# сложность и минимальные накладные расходы при обработке небольшого количества элементов.
# Адаптивность. Сортировка вставками адаптивна, что означает, что её производительность 
# может улучшаться для частично упорядоченных данных. Она может быстро обрабатывать 
# уже отсортированные или почти отсортированные списки.

# Недостатки алгоритма сортировки вставками
# Квадратичная сложность алгоритма. Время выполнения растёт пропорционально квадрату 
# количества элементов, что может привести к плохой производительности при больших 
# наборах данных.
# Зависимость от исходного порядка. Алгоритм неэффективен при обратно отсортированных 
# данных или данных, где элементы уже находятся на своих местах.
# Неустойчивость. Может изменять относительный порядок элементов с одинаковыми 
# значениями, если это важно для конкретной задачи.

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]  # Берём текущий элемент, который нужно вставить в отсортированную часть списка
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперёд
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key  # Вставляем key в правильное место
# Пример использования
numbers = [5, 3, 8, 2, 1]
insertion_sort(numbers)
print(numbers)   # Вывод: [1, 2, 3, 5, 8]

# =======================================================================================

# 