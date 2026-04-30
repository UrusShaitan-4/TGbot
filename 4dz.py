# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує
# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали
# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()

class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        travel_time = distance / self.speed
        print(f"Прибыли в {destination}. Время в пути составило {travel_time:.2f} ч.")


class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.capacity = capacity
        self.passengers = []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пассажир {passenger.name} сел в автобус.")
        else:
            print(f"Мест нет! Пассажир {passenger.name} не смог сесть.")

    def move(self, destination, distance):
        still_on_board = []
        count_left = 0

        for p in self.passengers:
            if p.destination == destination:
                count_left += 1
            else:
                still_on_board.append(p)

        self.passengers = still_on_board

        print(f"На остановке {destination} вышло пассажиров: {count_left}")
        super().move(destination, distance)

my_bus = Bus(speed=60, capacity=2)

p1 = Passenger("Иван", "Центр")
p2 = Passenger("Мария", "Вокзал")
p3 = Passenger("Алексей", "Центр")

my_bus.board_passenger(p1)
my_bus.board_passenger(p2)
my_bus.board_passenger(p3)

my_bus.move("Центр", 15)

print(f"Осталось пассажиров в салоне: {len(my_bus.passengers)}")
