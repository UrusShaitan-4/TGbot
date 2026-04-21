
from abc import ABC
from enum import Enum

from uuid import uuid4


class RobotStatus(Enum):
    off = "off"
    on = "on"

class Robot(ABC):
    def __init__(self, name:str = None,
                 battery_level:int = 100,
                 status: RobotStatus = RobotStatus.off):
        if name is None:
            name = str(uuid4())
        self.name = name
        self.battery_level = battery_level
        self.status = status

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Уровень заряда {self.battery_level}%")
        print(f"Статус: {self.status.value}")


    def charge(self):
        self.battery_level = 100

    def turn_on(self):
        self.status = RobotStatus.on

    def turn_off(self):
        self.status = RobotStatus.off

robot1 = Robot()
robot1.info()

# Завдання 2
# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
# Практичне завдання
#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy
class CleaningMode(Enum):
    dry = "dry"
    wet = "wet"
class CleaningRobot(Robot):
    def __init__(self, name:str,
                 cleaning_mode: CleaningMode,
                 battery_level:int=100,
                 dust_level:int=0,
                 water_level:int=100
                 ):
        super().__init__(name,battery_level)
        self._dust_level = dust_level
        self._water_level = water_level
        self._cleaning_mode = cleaning_mode

    def info(self):
        super().info()
        print(f"Cleaning mode: {self._cleaning_mode.name}")
        print(f"Dust level: {self._dust_level}")
        print(f"Water level: {self._water_level}")

    def turn_on(self):
        if self._dust_level == 100:
            print(f"{self.name} conteiner is full")
            return
        
        if self._water_level == 0 and self._cleaning_mode == CleaningMode.wet:
            print(f"{self.name} water is empty")
            return
        
        super().turn_on()

    def empty_dustbin(self):
        self._dust_level = 0
        print(f"{self.name} dust bin is empty")

    def fill_water(self):
        self._water_level = 100
        print(f"{self.name} water level is 100")

    def swap_mode(self):
        if self._cleaning_mode == CleaningMode.dry:
            self._cleaning_mode = CleaningMode.wet
        else:
            self._cleaning_mode = CleaningMode.dry

    def clean(self, energy: int, dust: int, water=None):
        if self.status == "off":
            print(f"{self.name} Cleaning is off")
            return

        if water is None and self._cleaning_mode == CleaningMode.wet:
            print(f"{self.name} Cleaning is off")
            return

        if self._cleaning_mode == CleaningMode.wet and self._water_level < water:
            print(f"{self.name} Cleaning is off")
            return

        if self._dust_level + dust > 100:
            print(f"{self.name} Cleaning is off")
            return

        if self.battery_level < energy:
            print(f"{self.name} Cleaning is off")
            return

        self._dust_level += dust
        if self._cleaning_mode == CleaningMode.wet:
            self._water_level -= water

        self.battery_level -= energy

# Створіть дочірній клас SecurityRobot
# Додаткові атрибути:
#  min_speed – мінімальна швидкість руху, щоб помітити
# об’єкт
#  alert_level – рівень небезпеки (low, middle, high)
#  dangerous_items – список небезпечних предметів(gun,
# knife, bat)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_off() – перед виключенням змінює рівень небезпеки
# на low
#  add_dangerous_item(item) – додає небезпечний предмет
#  remove_dangerous_item(item) – видаляє небезпечний
# предмет
#  detect(speed, item) – виявляє загрозу
# o якщо швидкість занизька, то ігноруємо
# o якщо швидкість велика, то рівень небезпеки
# middle
# o якщо це небезпечний предмет, то рівень
# небезпеки high
# Рівень небезпеки не може стати нижчим
from typing import List

class AlertLevel(Enum):
    low = "low"
    middle = "middle"
    high = "high"

class SecurityRobot(Robot):
    def __init__(
            self, name: str,
            min_speed: int,
            alert_level: AlertLevel,
            dangerous_items: List[str] = None,
            battery_level: int = 100,
            status: RobotStatus = RobotStatus.off,
    ):
        super().__init__(name, battery_level, status)

        self._alert_level = alert_level
        self._min_speed = min_speed

        if dangerous_items is None:
            self._dangerous_items = []
        else:
            self._dangerous_items = dangerous_items

    def info(self):
        super().info()
        print(f"Мінімальна швидкість виявлення: {self.min_speed}")
        print(f"Рівень тривоги: {self.alert_level.name}")
        print(f"Список небезпечних предметів: {', '.join(self.dangerous_items)}")