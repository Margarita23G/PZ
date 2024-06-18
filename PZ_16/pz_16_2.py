# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы-
# наследники будут иметь свои уникальные свойства и методы.

import math


class Vehicle:
    def __init__(self, num_wheels, engine_power, weight, transmission_coeff=0.5):
        self.engine_power = engine_power
        self.weight = weight
        self.transmission_coeff = transmission_coeff
        self.num_wheels = num_wheels
        self.speed = self.calculate_max_speed()

    def calculate_max_speed(self):
        max_speed = math.sqrt((self.engine_power * self.transmission_coeff * 10) / (self.weight * 0.001)) * 3.6
        return max_speed

    def display_info(self):
        print(f"Средняя скорость: {self.speed} км/ч")
        print(f"Количество колес: {self.num_wheels}")


class Car(Vehicle):
    def __init__(self, engine_power, weight, num_doors, transmission_coeff=0.5):
        super().__init__(4, engine_power, weight, transmission_coeff)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Количество дверей: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, engine_power, weight, has_sidecar, transmission_coeff=0.3):
        super().__init__(2, engine_power, weight, transmission_coeff)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Есть ли коляска: {'Да' if self.has_sidecar else 'Нет'}")


if __name__ == '__main__':
    # Создание объектов классов
    vehicle = Vehicle(4, 150, 240)
    car = Car(150, 1600, 4)
    motorcycle = Motorcycle(35, 170, True)

    print("Ходовая часть:")
    vehicle.display_info()
    print("\nМашина:")
    car.display_info()
    print("\nМотоцикл:")
    motorcycle.display_info()
