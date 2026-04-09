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
#         self._used_memory = 0
#         self._is_on = False
#         self._apps = {}
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