# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# Домашнє завдання
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5

from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name, satiety=50, energy=50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100
        print(f"{self.name} поспал(а). Энергия: {self.energy}")

    def eat(self, food_amount):
        self.satiety = min(self.satiety + food_amount)
        if self.satiety > 100:
            self.satiety = 100
        print(f"{self.name} поел(а). Сытость: {self.satiety}")

    @abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass

class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy = max(0, self.energy - 2 * activity_level)
            self.satiety = max(0, self.satiety - activity_level)
            print(f"Кот {self.name} поиграл. Энергия: {self.energy}, Сытость: {self.satiety}")
        else:
            print(f"Кот {self.name} слишком голоден для игр!")

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"{self.name} поймал(а) мышь!")
            if self.satiety > 40:
                print("Кот играет с мышью.")
            else:
                print("Кот ест мышь.")
                self.eat(15)
        else:
            print(f"{self.name} слишком устал(а), чтобы ловить мышей.")

class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy = max(0, self.energy - activity_level // 2)
            self.satiety = max(0, self.satiety - activity_level // 2)
            print(f"Пес {self.name} поиграл. Энергия: {self.energy}, Сытость: {self.satiety}")
        else:
            print(f"Пес {self.name} хочет есть, а не играть!")

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.satiety > 10:
            self.energy = max(0, self.energy - 5)
            print(f"{self.name} принес мяч! Энергия: {self.energy}")
        else:
            print(f"{self.name} голоден и игнорирует мяч.")


my_cat = Cat("Мурка", satiety=70, energy=50)
my_dog = Dog("Шарик", satiety=20, energy=60)

my_cat.make_sound()
my_cat.play(10)
my_cat.catch_mouse()

print()
print()

my_dog.make_sound()
my_dog.play(5)
my_dog.fetch_ball()