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
#     def get_area(self):
#         p = 3.14
#         s = p*pow(self.radius,2)
#
#         return s
#
# colo1 = Circle(5)
# colo2 = Circle(10)
#
# result1 = colo1.get_area()
# result2 = colo2.get_area()
# print(result1)
# print(result2)

# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

# class BankAccount:
#
#     def __init__(self,owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print(f"{self.owner}: You cannot deposit negative amount")
#
#     def withdraw(self, amount):
#         if amount > 0 and amount < self.balance:
#             self.balance -= amount
#         else:
#             print(f"{self.owner}: You cannot withdraw not amount")
#
#     def info(self):
#         print(f"{self.owner}: Balance ${self.balance}")
#
# client_1 = BankAccount("Bob", 1000)
# client_2 = BankAccount("Alice", 5000)
# client_3 = BankAccount("Tom", 500)
#
# client_1.deposit(2000)
# client_1.info()
# client_1.withdraw(12500)
# client_1.info()