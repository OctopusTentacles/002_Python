# Задача 02. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля: 
# «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов). 
# Затем создайте список из десяти студентов 
# (данные о студентах можете придумать свои или запросить их у пользователя) 
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.


class Student:
    def __init__(self, index):
        self.index = index
        self.name = ''
        self.group_num = ''
        self.grade = []
        self.avarage_grade = 0

# вывод информации о студенте:
    def print_info(self, index):
        # grade = ''.join(str(self.grade))
# фу, намучился с format:<25...не мог правильно синтаксис прописать )))))
        print(f'{index:<3} Фамилия Имя: {self.name:<25}'
              f'Номер группы: {self.group_num:<8}'
              f'Успеваемость: {self.grade}')
        


        

class Team:
# создание группы студентов:
    def __init__(self, count):
        self.students = [Student(index) for index in range(1, count + 1)]

# заполнение иформации о студентах:
    def student_info(self):
        for student in self.students:
            student.name = input(f'\nВведите ФИ студента {student.index}: ')
            student.group_num = input('Введите номер группы: ')
# при вводе оценок нужно поймать исключение ValueError,
# while True ))) - долго мучился без него, не сразу дошло:
            for i in range(1, 6):
                while True:
                    try:
                        score = int(input(f'{i} оценка студента {student.name}: '))
                        student.grade.append(score)
                    except ValueError:
                        print('Введите целое число!')
                        continue
                    break    

# вывод информации всей группы:
    def print_all_info(self):
        print()
        for index, student in enumerate(self.students):
            student.print_info(index + 1)

    def selection_sort(self):
        for student in self.students:
            student.avarage_grade = int(sum(student.grade) / len(student.grade))

        for i_min in range(len(self.students)):
            for curr in range(i_min, len(self.students)):
# как-то сложно для меня это получается, тяжело осмыслить 
# как правильно написать...методом тыка - 2 дня (((
                if self.students[curr].avarage_grade < \
                    self.students[i_min].avarage_grade:
                    self.students[curr], self.students[i_min] = \
                        self.students[i_min], self.students[curr]
                    


students = Team(3)
students.student_info()
students.print_all_info()
students.selection_sort()
students.print_all_info()
