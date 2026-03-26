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
# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.

# class Car:
#
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#         self.is_ready = False
#
#
#     def start_engine(self):
#         if not self.is_ready:
#             self.is_ready = True
#             print(f"Двигатель с маркой авто: {self.brand} - запущен!")
#
#     def move(self):
#         if self.is_ready:
#             print(f"Автомобиль с маркой : {self.brand} поехал!")
#         else:
#             print(f"Автомобиль с маркой : {self.brand} не заведен!")
#
# auto1 = Car("Toyota", 5)
# auto2 = Car("Opel", 11)
#
# auto2.start_engine()
# auto1.move()
# auto2.move()

# Завдання 1 — Клас `BankCard` з лімітами та пін-кодом
#
# Створіть клас **BankCard** з атрибутами:
#
# *   `owner` — власник картки
# *   `balance` — поточний баланс
# *   `pin` — пін-код
# *   `daily_limit` — денний ліміт зняття грошей
# *   `withdrawn_today` — сума вже знятих за поточний день
#
# **Методи:**
#
# 1.  **Метод авторизації по пін-коду**
#     *   Логіка: перевіряє, чи співпадає введений код з піном картки. Якщо ні — доступ до операцій заборонено.
#     *   Параметри:
#         *   `self`
#         *   `entered_pin` — введений користувачем пін-код
#
# 2.  **Метод поповнення рахунку**
#     *   Логіка: додає суму до балансу, але тільки якщо користувач уже авторизований.
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума поповнення
#
# 3.  **Метод зняття грошей**
#     *   Логіка:
#         *   перевірити, чи авторизований користувач
#         *   перевірити, чи вистачає грошей на балансі
#         *   перевірити, чи не буде перевищено `daily_limit`
#         *   якщо все ок — зменшити баланс і збільшити `withdrawn_today`
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума для зняття
#
# 4.  **Метод скидання денного ліміту** (наприклад, на початку нового дня)
#     *   Логіка: обнуляє `withdrawn_today`.
#     *   Параметри:
#         *   `self`
#

# class BankCard:
#
#     def __init__(self, owner, balance, pin):
#         self.owner = owner
#         self.balance = balance
#         self.pin = pin
#         self.daily_limit = 10000
#         self.withdrawn_today = 0
#
#     def check_pin(self, entered_pin):
#         if entered_pin == self.pin:
#             return True
#         else:
#             return False
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Счет пополнен на {amount}")
#         else:
#             print(f"{self.owner}: You cannot deposit negative amount")
#
#     def show_info(self):
#         print(f"{self.owner}'s balance is {self.balance}")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сумма должна быть больше нуля.")
#         elif amount > self.balance:
#             print("Недостаточно средств на счете.")
#         elif self.withdrawn_today + amount > self.daily_limit:
#             print(f"Превышен дневной лимит! Осталось доступно на сегодня: {self.daily_limit - self.withdrawn_today}")
#         else:
#             self.balance -= amount
#             self.withdrawn_today += amount
#             print(f"Вы сняли: {amount}")
#
# user = BankCard("Bob", 1000, "0000")
#
#
# while True:
#     pin_input = input("Enter a pin number: ")
#
#     if pin_input == "exit":
#         break
#
#     if user.check_pin(pin_input):
#         print("Pin is valid")
#         user.show_info()
#
#         event = input("Выберите снять(1) либо добавить деньги(2): ")
#         amount = int(input("Введите сумму:"))
#
#         if event == "2":
#             user.deposit(amount)
#         elif event == "1":
#             user.withdraw(amount)
#         else:
#             print("Нет такой операции")
#
#         user.show_info()
#     else:
#         print("Invalid pin number")


