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
        key = lst[i]  # Берём текущий элемент, который нужно вставить в 
                        # отсортированную часть списка
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

# Shell sort
# Сортировка Шелла (Shell sort) — это алгоритм, который применяет сортировку вставками 
# к диапазонам элементов с определённым шагом. Шаг постепенно уменьшается, 
# позволяя элементам быстрее перемещаться в свои конечные позиции. 
# Таким образом, сортировка Шелла — это усовершенствованный вариант сортировки вставками.

# Преимущества сортировки Шелла
# Универсальность. Эффективна для разных размеров и типов данных. Она может улучшить 
# производительность сортировки для широкого спектра случаев, включая те, 
# где список частично упорядочен или содержит много элементов.
# Улучшенная производительность. Устраняет недостатки сортировки вставками и 
# обеспечивает более быстрое перемещение элементов в конечные позиции. Путём сортировки 
# подсписков с шагом, уменьшающимся на каждой итерации, она обеспечивает более 
# равномерное распределение элементов.
# Адаптивность. Сортировка Шелла адаптивна и может эффективно работать с разными 
# уровнями упорядоченности данных. Она способна эффективно справляться с небольшими 
# изменениями или частичной упорядоченностью данных, что делает её гибким алгоритмом.

# Недостатки алгоритма
# Сложность выбора интервалов. Требует определения последовательности интервалов, 
# что может быть сложной задачей и влиять на производительность. В частности из-за 
# этого точная оценка производительности алгоритма может быть нетривиальной задачей.
# Неустойчивость. Не гарантирует сохранения относительного порядка элементов с 
# одинаковыми значениями.

def shell_sort(lst):
    n = len(lst)
    gap = n // 2  # Инициализация начального значения интервала
    while gap > 0:
        # Применяем сортировку вставками с заданным интервалом
        for i in range(gap, n):
            temp = lst[i]
            j = i
            # Сдвигаем элементы, чтобы найти правильную позицию для вставки элемента
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2  # Уменьшаем интервал
    return lst
# Пример использования
numbers = [8, 3, 1, 5, 2]
sorted_numbers = shell_sort(numbers)
print(sorted_numbers)  # Вывод: [1, 2, 3, 5, 8]

# =======================================================================================

# selection sort
# Сортировка выбором (selection sort) — это простой алгоритм сортировки, который на 
# каждом шаге находит минимальный или максимальный элемент из неотсортированной части 
# списка и помещает его в начало или конец отсортированной части.

# Преимущества сортировки выбором
# Простота реализации. Это один из самых простых алгоритмов сортировки для понимания 
# и реализации. Требует только базовых операций сравнения и перестановки элементов.
# Потребление памяти. Работает непосредственно со списком, не требуя памяти для 
# хранения дополнительных структур данных.
# Устойчивость. Сортировка выбором устойчива, что означает, что она сохраняет 
# относительный порядок элементов с одинаковыми значениями.

# Недостатки алгоритма сортировки выбором
# Квадратичная сложность времени. Время выполнения алгоритма растёт пропорционально 
# квадрату количества элементов, что делает его неэффективным для больших наборов данных.
# Ограниченная эффективность. По сравнению с некоторыми другими алгоритмами сортировки, 
# сортировка выбором обычно менее эффективна и требует больше операций сравнения 
# и обмена элементов.

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        # Находим индекс минимального элемента в неотсортированной части списка
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Меняем местами минимальный элемент с первым элементом неотсортированной части
        lst[i], lst[min_index] = lst[min_index], lst[i]
# Пример использования
numbers = [5, 3, 8, 2, 1]
selection_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]

# =======================================================================================

# Merge sort
# Сортировка слиянием (merge sort) — это алгоритм сортировки, который использует 
# стратегию «разделяй и властвуй». Он разбивает список на две половины, 
# рекурсивно сортирует каждую, а затем объединяет их в отсортированный список.

# Преимущества сортировки слиянием
# Стабильность. Сохраняет относительный порядок элементов с одинаковыми значениями. 
# Если в списке есть элементы с одинаковыми значениями, они останутся в том же порядке, 
# в котором находились в исходном списке.
# Гарантированная сложность O(n*log n). Это делает алгоритм эффективным для сортировки 
# больших объёмов данных.
# Применимость для связных структур данных. Хорошо работает с данными, хранящимися в 
# связных структурах, таких как связанные списки, поскольку не требует прямого доступа 
# к элементам по индексу.

# Недостатки алгоритма
# Дополнительное использование памяти. Требует дополнительной памяти для временного 
# хранения элементов во время слияния. Это может быть проблематично при работе с очень 
# большими наборами данных, особенно если доступ к дополнительной памяти ограничен.
# Сложность реализации. Алгоритм непросто реализовать, в частности требуется аккуратно 
# управлять процессами разделения и слияния массива.

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # Разделяем список на две половины
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Объединяем отсортированные половины в один список
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        # Сравниваем элементы из обоих списков и добавляем меньший в объединённый список
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Добавляем оставшиеся элементы из левого списка
    merged.extend(left[left_index:])
    # Добавляем оставшиеся элементы из правого списка
    merged.extend(right[right_index:])
    return merged
# Пример использования
numbers = [8, 3, 1, 5, 2]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Вывод: [1, 2, 3, 5, 8]

# =======================================================================================

# Bucket sort
# Карманная сортировка (bucket sort) — это алгоритм сортировки, который разбивает 
# список на равные интервалы, называемые карманами, а затем сортирует элементы в каждом 
# кармане отдельно. Затем элементы из всех карманов объединяются, чтобы получить 
# окончательно отсортированный список.

# Преимущества карманной сортировки
# Эффективность для равномерно распределённых данных. Эффективна для данных, 
# которые равномерно распределены в пределах заданного диапазона. Она работает особенно 
# хорошо, когда входные данные равномерно распределены по интервалу значений.
# Лёгкость реализации. Карманная сортировка относительно проста в реализации. 
# Она требует только основных операций вставки и извлечения элементов из карманов.
# Подходит для внешней сортировки. Хорошо подходит для сортировки данных, 
# которые не могут поместиться в оперативную память и требуют внешней сортировки. 
# Она может использоваться в комбинации с другими алгоритмами, чтобы обработать 
# большие объёмы данных.

# Недостатки алгоритма
# Зависимость от диапазона значений. Алгоритм карманной сортировки эффективен только 
# при ограниченном диапазоне значений, что делает его неэффективным для сортировки 
# больших наборов данных с широким диапазоном значений.
# Дополнительное использование памяти. Алгоритм требует дополнительной памяти для 
# создания и управления карманами, особенно если количество возможных значений велико 
# или неизвестно заранее.
# Неустойчивость. Карманный алгоритм сортировки может изменять относительный порядок
# элементов с одинаковыми значениями.

def bucket_sort(lst):
    # Определяем количество карманов
    num_buckets = len(lst)
    # Создаём пустые карманы
    buckets = [[] for _ in range(num_buckets)]
    # Распределяем элементы по карманам
    for num in lst:
        index = int(num * num_buckets)  # Вычисляем индекс кармана для текущего элемента
        buckets[index].append(num)
    # Сортируем каждый карман отдельно
    for bucket in buckets:
        bucket.sort()
    # Объединяем элементы из всех карманов
    sorted_lst = []
    for bucket in buckets:
        sorted_lst += bucket
    return sorted_lst
# Пример использования
numbers = [0.42, 0.25, 0.75, 0.12, 0.9]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)  # Вывод: [0.12, 0.25, 0.42, 0.75, 0.9]

