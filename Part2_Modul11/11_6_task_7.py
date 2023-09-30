# Задача 07. Матрицы
# Контекст
# Вы стажируетесь в лаборатории искусственного интеллекта, 
# в ней вам поручили разработать класс Matrix для обработки и анализа данных. 
# Ваш класс должен предоставлять функциональность для выполнения основных 
# операций с матрицами, таких как сложение, вычитание, умножение и транспонирование. 
# Это будет полезно для обработки и структурирования больших объёмов данных, 
# которые используются в обучении нейронных сетей.

# Задача
# Создайте класс Matrix для работы с матрицами. Реализуйте методы:
# сложения,
# вычитания,
# умножения,
# транспонирования матрицы.
# Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.

# Советы
# Методы сложения/вычитания/умножения должны получать параметром другую матрицу 
# (объект класса Matrix) и выполнять указанное действие над

# своей и этой другой матрицей. Например, метод сложения должен получить параметром 
# новую матрицу и сложить её со своей текущей.

# Метод транспонирования не должен ничего получать, он должен работать исключительно со своей матрицей.

# Транспонирование — это алгоритм, при котором строки матрицы меняются местами с её столбцами:
# Создать новую матрицу result с размерами, обратными размерам исходной матрицы. 
# Количество строк новой матрицы равно количеству столбцов исходной, 
# а количество столбцов новой матрицы равно количеству строк исходной.

# Пройтись по каждому элементу исходной матрицы. Для каждого элемента с индексами (i, j):
# Поместить значение этого элемента (i, j) в ячейку с индексами (j, i) новой матрицы. 
# То есть транспонирование происходит с помощью обмена индексов местами.
# После завершения цикла новая матрица result будет содержать транспонированную матрицу, которую можно вернуть.

# Пример:
# Создание экземпляров класса Matrix
# m1 = Matrix(2, 3)
# m1.data = [[1, 2, 3], [4, 5, 6]]


# m2 = Matrix(2, 3)
# m2.data = [[7, 8, 9], [10, 11, 12]]


# # Тестирование операций
# print("Матрица 1:")
# print(m1)


# print("Матрица 2:")
# print(m2)


# print("Сложение матриц:")
# print(m1.add(m2))


# print("Вычитание матриц:")
# print(m1.subtract(m2))


# m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]


# Вывод:
# Матрица 1:
# 1	2	3
# 4	5	6

# Матрица 2:
# 7	8	9
# 10	11	12

# Сложение матриц:
# 8	10	12
# 14	16	18

# Вычитание матриц:
# -6	-6	-6
# -6	-6	-6

# Умножение матриц:
# 22	28
# 49	64

# Транспонирование матрицы 1:
# 1	4
# 2	5
# 3	6


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = list()

    def __str__(self):
        show_matrix = str()
        for index in self.data:
            for value in index:
                show_matrix += '{:<5}'.format(value)
            show_matrix += '\n'
        return show_matrix

    def add(self, not_self):
        # self = m1, not_self = m2
        # print(self)
        # print(not_self)
        # надо создать новую матрицу для результата
        result_matrix = Matrix(self.rows, self.columns)
        result_matrix.data = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        # print(result_matrix.data)
        for row in range(self.rows):
            for col in range(self.columns):
                # print(self.data[row][col] + not_self.data[row][col])
                # self.data[row][col] = self.data[row][col] + not_self.data[row][col]
                result_matrix.data[row][col] = self.data[row][col] + not_self.data[row][col]
        # return self
        return result_matrix

    def subtract(self, not_self):
        result_matrix = Matrix(self.rows, self.columns)
        result_matrix.data = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.columns):
                result_matrix.data[row][col] = self.data[row][col] - not_self.data[row][col]
        return result_matrix
    


    def multiply(self, not_self):
        result_matrix = Matrix(self.rows, self.columns)
        result_matrix.data = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        print(self.data)
        print(not_self.data)
        for row in range(self.rows):
            for col in range(self.columns):
                result_matrix.data[row][col] = self.data[row][col] * not_self.data[row][col]

        # result_matrix.data = [row * col for row, col in zip(self.data, not_self.data)]

        print(result_matrix.data)

    def transpose():

        pass


# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))
# для проверки, что матрицы не меняются
# print(m1)
# print(m2)

print("Вычитание матриц:")
print(m1.subtract(m2))
# для проверки, что матрицы не меняются
# print(m1)
# print(m2)


m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
print("Матрица 3:")
print(m3)


print("Умножение матриц:")
print(m1.multiply(m3))

# print("Транспонирование матрицы 1:")
# print(m1.transpose())