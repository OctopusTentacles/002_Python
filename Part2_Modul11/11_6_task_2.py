# Задача 02. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля: 
# «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов). 
# Затем создайте список из десяти студентов 
# (данные о студентах можете придумать свои или запросить их у пользователя) 
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.


class Student:

    def __init__(self, name, group_num='', grade=[]):
        self.name = name
        self.group_num = group_num
        self.grade = grade

# вывод информации о студенте:
    def print_info(self):
        print(f'Фамилия Имя: {self.name}. '
              f'Номер группы: {self.group_num}. '
              f'Успеваемость: {self.grade}')
        

class Team:

# создание группы студентов:
    def __init__(self, count):
        self.students = [Student(index) for index in range(1, count + 1)]

# заполнение иформации о студентах:
    def student_info(self):
        for student in self.students:
            student.name = input('\nВведите имя студента: ')
            student.group_num = input('Введите номер группы: ')
            for i in range(1, 6):
                try:
                    score = int(input(f'{i} оценка студента {student.name}: '))
                    if score is not int:
                        raise ValueError('Введите число!')
                    else:
                        student.grade.append(score)

                except ValueError as exc:
                    print(exc)
                    
                    

        
        student.print_info()
    


# вывод информации всей группы:
    def print_all_info(self):
        for student in self.students:
            student.student_info()



students = Team(10)
students.student_info()