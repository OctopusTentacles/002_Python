# Задача 02. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля: 
# «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов). 
# Затем создайте список из десяти студентов 
# (данные о студентах можете придумать свои или запросить их у пользователя) 
# и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.


class Student:

    def __init__(self, name, group_num='10A', grade=[4, 5, 4, 3, 5]):
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


    
# вывод информации всей группы:
    def print_all_info(self):
        for student in self.students:
            student.print_info()



students = Team(10)
students.print_all_info()