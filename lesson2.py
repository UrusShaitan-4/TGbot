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
# from typing import List
#
# class Project:
#     def __init__(self, name: str, budget: int):
#         self.name: str = name
#         self.budget: int = budget
#         self.total_expenses: int = 0
#         self.is_completed: bool = False
#         self.duration_months: int = 0
#         self.tasks: List[str] = []
#
#     def display_info(self):
#         print(f"\nПроект: {self.name} | Время: {self.duration_months} мес.")
#         print(f"Бюджет: {self.budget} | Затраты: {self.total_expenses}")
#         print("Задачи:", ", ".join(self.tasks) if self.tasks else "Нет задач")
#
#     def add_task(self, task_name: str):
#         self.tasks.append(task_name)
#
#     def split_task(self, task_name: str, subtasks: List[str]):
#         self.tasks.remove(task_name)
#         self.tasks.extend(subtasks)
#
#     def complete_task(self, task_name: str, time: int, cost: int):
#         for i, task in enumerate(self.tasks):
#             if task==task_name:
#                 self.total_expenses += cost
#                 self.duration_months += time
#                 self.tasks.pop(i)
#                 if self.total_expenses > self.budget:
#                     print("Превышение бюджета!")
#                 return
#         print(f"Задача {task_name} не найдена")
#
#     def top_up_budget(self, amount: int):
#         if amount > 0:
#             self.budget += amount
#             print(f"Пополнено на {amount}")
#
#
# my_project = Project("Приложение", 50000)
# my_project.add_task("Интерфейс")
# my_project.add_task("Логика")
#
# my_project.split_task("Логика", ["БД", "Сеть"])
# my_project.display_info()
#
# my_project.complete_task("Интерфейс", 2, 10000)
# my_project.top_up_budget(5000)
#
# my_project.display_info()
#
# Завдання 2

# Додайте методи:



#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

from typing import  Dict

class Phone:
    def __init__(self, max_memory: int):
        self.max_memory = max_memory
        self.used_memory: int = 0
        self.is_on: bool = False
        self.apps: Dict[str,int] = {}

    def show_info(self):
        status = "Ввімкнено" if self.is_on else "Вимкнено"
        print("--- Інформація про телефон ---")
        print(f"Статус: {status}")
        print(f"Пам'ять: {self.used_memory} / {self.max_memory} МБ")

        if self.apps:
            print("Встановлені додатки:")
            for name, size in self.apps.items():
                print(f" - {name}: {size} МБ")
        else:
            print("Встановлених додатків немає.")
        print("------------------------------")

    def install_app(self, app: str, size: int):
        if self.used_memory + size > self.max_memory:
            print("Недостаточно памяти")
            return

        self.apps[app] = size
        self.used_memory += size

    def delete_app(self, app: str):
        if app in self.apps:
            size = self.apps.pop(app)
            self.used_memory -= size



phone1 = Phone(126)
phone1.show_info()
phone1.install_app("TG", 20)
phone1.install_app("Google", 10)

phone1.show_info()
phone1.delete_app("TG")
phone1.show_info()













