# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»
# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.
# class Student:
#
#     def __init__(self, name, age):
#         self.name = name.capitalize()
#         self.age = age
#
#     def show_info(self):
#         print(f"Имя: {self.name}, возраст: {self.age}")
#
# students = []
#
# student1 = Student("Tom", 21)
# student2 = Student("Bob", 22)
# student3 = Student("Tim", 19)
#
# students.append(student1)
# students.append(student2)
# students.append(student3)
#
# for stud in students:
#     stud.show_info()

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

# class Circle:
#
#     def __init__(self, radius = 0):
#         self.radius = radius
#
#     def s_circle(self):
#         p = 3.14
#         s = p*pow(self.radius,2)
#
#         return s
#
# colo1 = Circle(5)
# colo2 = Circle(10)
#
# result1 = colo1.s_circle()
# result2 = colo2.s_circle()
# print(result1)
# print(result2)
#