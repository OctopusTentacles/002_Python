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
        
        # self     2-rows, 3-cols   [[1, 2, 3], [4, 5, 6]]
        # not-self 3-rows, 2-cols   [[1, 2], [3, 4], [5, 6]]
        # need     2-rows, 2-cols  
        # 
        # получается надо умножать строку на столб: 
        #               
        # 123   12   1*1 2*3 3*5 | 1*2 2*4 3*6
        # 456   34   4*1 5*3 6*5 | 4*2 5*4 6*6 
        #       56
        # 
        # и сложить:
        # 
        # 1*1 + 2*3 + 3*5 | 1*2 + 2*4 + 3*6
        # 4*1 + 5*3 + 6*5 | 4*2 + 5*4 + 6*6
        # 
        # 0:0*0:0 + 0:1*1:0 + 0:2*2:0 | 0:0*0:1 + 0:1*1:1 + 0:2*2:1
        # 1:0*0:0 + 1:1*1:0 + 1:2*2:0 | 1:0*0:1 + 1:1*1:1 + 1:2*2:1

        result_matrix = Matrix(self.rows, not_self.columns)
        result_matrix.data = [[0 for _ in range(result_matrix.columns)] 
                            for _ in range(result_matrix.rows)]
        # print(self.data)
        # print(not_self.data)
        # print(result_matrix.data)
    
        for row in range(self.rows):
            for col in range(not_self.columns):
                cell = 0
                for cols in range(self.columns):
                    cell += self.data[row][cols] * not_self.data[cols][col]
                result_matrix.data[row][col] = cell

                # for colum in range(self.columns):
                #     result_matrix.data[row][col] = self.data[row][colum] * not_self.data[colum][col]
        # result_matrix.data = [row * col for row, col in zip(self.data, not_self.data)]
        return result_matrix

    def transpose():
        
        # 2-rows, 3-cols == 3-rows, 2-cols

        # [[1, 2, 3], [4, 5, 6]] == [[1, 4], [2, 5], [3, 6]]
         
        # 1 2 3     1 4
        # 4 5 6     2 5
        #           3 6

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

print("Транспонирование матрицы 1:")
print(m1.transpose())


# multiply понравилось!!! пока не расписал все - ответ не получался!!! 