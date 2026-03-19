import string_utils as s
import math
import time
from datetime import date

def main():
    string_a = input("Enter string:")
    print("Строка без символов: ", s.del_chars(string_a))
    print("Количество гласных букв: ",s.count_glasn(string_a))
    print("Палиндром или нет:", s.pallindrom(string_a))

def triangle_area(a,b, angle_degrees):

    angle_radians = math.radians(angle_degrees)
    area = 0.5 * a * b * math.sin(angle_radians)

    return area


def sum_numbers():

    start_time = time.time()

    summa = 0
    for i in range(1, 10000000+1):
        summa += i

    end_time = time.time()

    work_time= end_time - start_time
    return work_time, summa

def age_user():
    birth_date =input("Введите дату рождения в формате YYYY-MM-DD:")
    birth_date =birth_date.split("-")
    year, month, day = int(birth_date[0]), int(birth_date[1]), int(birth_date[2])
    birth_date = date(year, month, day)
    today = date.today()
    age = (today - birth_date).days // 365
    return age

if __name__ == "__main__":

    # main()

    #   Завдання 2
    # Напишіть функцію для обрахунку площі трикутника по
    # формулі
    #  ( )
    # Параметри функції: сторони a і b та кут . Функцію синус
    # візьміть з модуля math
    # calculate = triangle_area(20,15,45)
    # calculate = round(calculate,2)
    # print(calculate)

# Завдання 3
# Напишіть функцію, яка обчислює суму чисел від 1 до 10
# млн. Виведіть час роботи програми.
# Див time.time()
#     time_work, summa = sum_numbers()
#     print(f"Времмя роботы - {time_work}, сумма чисел = {summa}")


    # Завдання 4
    # Користувач вводить свою дату народження у форматі
    # YYYY-MM-DD. Виведіть вік користувача.
    # Див datetime.date.fromisoformat()
    #  datetime.date.today()
    #  datetime.timedelta.days

    print(age_user())

