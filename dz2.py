# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису
# class Project:
#     def __init__(self,project_name: str, budget: int, total_casts: int,tasks: list, duration_months:int = 0):
#         self._project_name = project_name
#         self._budget = budget
#         self._total_casts = total_casts
#         self._is_completed = False
#         self._duration_months = duration_months
#         self._tasks = tasks
#
#     def show_info(self):
#         print(f"Проэкт: {self._project_name} |  Время выполнения: {self._duration_months} месяцев")
#         print(f"Бютжет: {self._budget} | Использовано: {self._total_casts}")
#         print("Задачи: ")
#         for task in self._tasks:
#             print(f"{task}")
#
#     def add_task(self, name_task):
#         if name_task not in self._tasks:
#             self._tasks.append(name_task)
#
#     def split_task(self, task_name, subtask_list):
#         if task_name in self._tasks:
#             index = self._tasks.index(task_name)
#             for i, subtask in enumerate(subtask_list):
#                 self._tasks.insert(index + 1 + i, f"  --- {subtask}")
#
#     def finish_task(self, task_name, time_finished, amount):
#         if task_name in self._tasks:
#             index = self._tasks.index(task_name)
#             self._tasks[index] = f"{task_name} (Выполнена)"
#
#             if self._total_casts + amount <= self._budget:
#                 self._total_casts += amount
#             else:
#                 print("Не достаточно денег в бютжете! ")
#                 return
#
#             self._duration_months += time_finished
#
#             print(f"Задача '{task_name}' выполнена за {time_finished} мес. Списано: {amount}")
#         else:
#             print("Нет такой задачи!")
#
#     def add_budget(self,amount):
#         if amount > 0:
#             self._budget += amount
#
#
# task1 = Project("Построить дом", 100000,0,
#                 ["Привезти материалы", "Сделать фундамент", "Построить стены"] )
#
# task1.add_budget(10000)
# task1.split_task("Сделать фундамент", ["Выкопать яму", "Залить бетон"])
# task1.show_info()
# print()
# task1.finish_task("Построить стены", 3, 10000)
# print()
# task1.show_info()



# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

# class Phone:
#     def __init__(self, max_memory: int):
#         self._max_memory = max_memory
#         self._used_memory:int = 0
#         self._is_on: bool = False
#         self._apps: dict = {}
#
#     def show_status(self):
#         free_memory = self._max_memory - self._used_memory
#         print(f"Память: ")
#         print(f"Всего: {self._max_memory} МБ")
#         print(f"Занято: {self._used_memory} МБ")
#         print(f"Свободно: {free_memory} МБ")
#         print(f"Приложения: {list(self._apps.keys())}")
#
#     def add_app(self, app:str,size:int):
#         if self._used_memory+size <= self._max_memory:
#             if app not in self._apps:
#                 self._apps[app] = size
#                 self._used_memory += size
#                 print(f"Приложение '{app}' установлено ({size} МБ).")
#             else:
#                 print(f"Приложение '{app}' уже установлено.")
#
#     def delete_app(self, app):
#         if app in self._apps:
#             size = self._apps.pop(app)
#             self._used_memory -= size
#             print(f"Приложение '{app}' удалено. Освобождено {size} МБ.")
#         else:
#             print(f"Приложение '{app}' не найдено.")
#
#     def update_app(self, name, new_size):
#         if name in self._apps:
#             old_size = self._apps[name]
#             if (self._used_memory - old_size + new_size) <= self._max_memory:
#                 self._used_memory = self._used_memory - old_size + new_size
#                 self._apps[name] = new_size
#                 print(f"Приложение '{name}' обновлено. Новый размер: {new_size} МБ.")
#             else:
#                 print(f"Недостаточно места для обновления '{name}' до {new_size} МБ!")
#         else:
#             print(f"Приложение '{name}' не установлено, обновление невозможно.")
#
#     def turn_on(self):
#         self._is_on = True
#         print("Телефон включен.")
#
#     def turn_off(self):
#         self._is_on = False
#         print("Телефон выключен.")
#
#     def run_app(self, name):
#         if not self._is_on:
#             print("Ошибка: Сначала включите телефон!")
#             return
#
#         if name in self._apps:
#             print(f"Запуск приложения '{name}' Успешно!")
#         else:
#             print(f"Ошибка: Приложение '{name}' не найдено.")
#
#
# phone15 = Phone(256)
# phone15.show_status()
# print()
# phone15.add_app("TG", 26)
# phone15.show_status()
# print()
# phone15.turn_on()
# phone15.run_app("TG")
# print()
# phone15.update_app("TG", 36)
# phone15.show_status()
# print()
# phone15.delete_app("TG")
# phone15.show_status()

# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км) 1 5
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального

# import random
# class Auto:
#     def __init__(self, brand:str,fuel_level:float, consumption:float, mileage:int = 0):
#         self._brand = brand
#         self._mileage = mileage
#         self._fuel_level = fuel_level
#         self._consumption = consumption
#         self._is_broken = True
#
#     def show_info(self):
#         print(f"Марка: {self._brand} | Пробег: {self._mileage}")
#         print(f"Показатель бензина {self._fuel_level} л.")
#         if self._is_broken:
#             print("Авто исправно!")
#         else:
#             print("Авто поломано!")
#
#     def move(self, size:int):
#         if self._is_broken:
#             fuel_size = size * self._consumption
#             if self._fuel_level >= fuel_size:
#                 print("Едем...")
#                 self._fuel_level -= fuel_size
#                 self._mileage += size
#         if random.random() < 0.4:
#             self._is_broken = False
#             print("Во время поездки отвалилось колесо...")
#         else:
#             print("Отремонтируй автомобиль!")
#
#     def repair(self):
#         if not self._is_broken:
#             self._is_broken = True
#             print("Починили колесо.")
#         else:
#             print("Авто в порядке - не требуется ремонт")
#
#     def add_fuel(self, amount):
#         if amount > 0:
#             self._fuel_level+=amount
#             print(f"Залили {amount} л. бенза")
#             print(f"В баке: {self._fuel_level} л.")
#
#
# auto1 = Auto("Audi", 5, 0.2)
# auto1.show_info()
# print()
# auto1.move(10)
# auto1.show_info()
# print()
# auto1.repair()
# auto1.show_info()
# print()
# auto1.add_fuel(15)

# Завдання 4
# Створіть клас Студент з атрибутами:
#  ім’я
#  словник з предметами, де ключ – назва предмету,
# значення – список оцінок
# Додайте методи:
#  додати новий предмет
#  видалити предмет
#  вчити предмет(якщо отримана оцінка, то додати про це
# інформацію)
#  отримати середню оцінку за конкретним предметом
#  вивести загальну інформацію: ім’я та список предметів
# з середніми оцінками

# class Student:
#     def __init__(self, name:str):
#         self._name = name
#         self._lesson: dict = {}
#
#     def add_lesson(self,lesson_name:str):
#         if lesson_name not in self._lesson:
#             self._lesson[lesson_name] = []
#             print(f"Предмет {lesson_name} добавлен! ")
#         else:
#             print("Предмет уже существует!")
#
#     def del_lesson(self, lesson_name:str):
#         if lesson_name in self._lesson:
#             self._lesson.pop(lesson_name)
#             print(f"Предмет {lesson_name} удален!")
#         else:
#             print("Нет такого предмета!")
#
#     def all_info(self):
#         print(f"Студент {self._name} | Предметы: {self._lesson}")
#
#     def study_lesson(self, lesson_name:str, grade:int):
#         if lesson_name in self._lesson:
#             self._lesson[lesson_name].append(grade)
#             print(f"Получена оценка {grade}, по предмету: {lesson_name}")
#
#     def get_avg(self, lesson_name:str):
#         if lesson_name in self._lesson:
#             grades = self._lesson[lesson_name]
#
#             if grades:
#                 avg = sum(grades)/len(grades)
#                 return avg
#             else:
#                 print("Нет оценок по предмету.")
#         else:
#             print("Нет такого предмета в списке.")
#             return
#
#
# student1 = Student("Bob")
# student1.add_lesson("Algebra")
# student1.add_lesson("Biologia")
# student1.all_info()
# student1.del_lesson("Biologia")
# student1.study_lesson("Algebra", 5)
# student1.all_info()
# print("Средний бал по Algebra:",student1.get_avg("Algebra"))

# Завдання 5
# Створіть клас Магазин з атрибутами:
#  назва
#  заробіток
#  словник з товарами, де ключ – назва товару, значення –
# кількість на складі
#  словник з товарами, де ключ – назва товару, значення –
# ціна
# Додайте методи:
#  вивід інформації: назва та список доступних товарів
#  поповнення складу певним товаром(може бути новий)
#  оформлення замовлення, якщо товар у достатній
# кількості доступний

class Store:
    def __init__(self, name: str):
        self._name = name
        self._revenue = 0.0
        self._inventory = {}
        self._prices = {}

    def show_info(self):
        print("Магазин: ", self._name)
        print("Товары на складе: ")
        for key, value in self._inventory.items():
            print(key, " - ", value)

    def add_item(self, item_name: str, quantity: int, price: float = None):
        if item_name in self._inventory:
            self._inventory[item_name] += quantity
        else:
            self._inventory[item_name] = quantity

        self._prices[item_name] = price

    def new_order(self, item_name: str, quantity: int):
        if item_name not in self._inventory:
            print(f"Ошибка: '{item_name}' нет такого товара.")
            return

        if self._inventory[item_name] >= quantity:
            price_unit = self._prices[item_name]
            total_cost = price_unit * quantity

            self._inventory[item_name] -= quantity
            self._revenue += total_cost

            print(f"Заказ оформлен! Продано '{item_name}' ({quantity} шт.) на сумму {total_cost}.")
        else:
            available = self._inventory[item_name]
            print(f"Недостаточно товара! Вы просите {quantity}, а в наличии всего {available}.")

my_shop = Store("ProTech")

my_shop.add_item("Соль", 10, 20)
my_shop.add_item("Сахар", 50, 10)
my_shop.add_item("Гречка", 110, 8)
my_shop.show_info()
my_shop.new_order("Соль",5)
my_shop.new_order("Сахар",60)
my_shop.new_order("Рис",5)

print()
print("Выручка:", my_shop._revenue)
