# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

# class Cart:
#     def __init__(self,client:str, items:list):
#         self._client = client
#         self._items = items
#
#     def add_item(self,new_product):
#         if new_product not in self._items:
#             self._items.append(new_product)
#
#     def delete_item(self,delete_product):
#         if delete_product in self._items:
#             self._items.remove(delete_product)
#
#     def show_info(self):
#         print(f"Имя клиента: {self._client}")
#         print(f"Список товаров: {self._items}")
#
# cart1 = Cart("Bob", ["Хлеб", "Соль", "Масло"])
# cart2 = Cart("Tom", ["Молоко", "Картошка"])
# cart1.show_info()
# cart1.add_item("Мясо")
# cart1.delete_item("Перец")
# cart1.delete_item("Соль")
# cart1.show_info()
#
# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.

class Phone:
    def __init__(self, number: int, battery_level: int = 100):
        self._number = number
        self._battery_level = battery_level

    def reduce_battery(self, value):
        if value < self._battery_level:
            if self._battery_level < 0:
                self._battery_level = 0

            self._battery_level = self._battery_level - value

            if self._battery_level <= 20:
                print("Низкий уровень заряда!")


    def show_info(self):
        print("Номер телефона: ", self._number)
        print("Заряд батареи: ", self._battery_level, "%")

phone_test = Phone(1231, 40)
phone_test.show_info()
phone_test.reduce_battery(25)
phone_test.show_info()