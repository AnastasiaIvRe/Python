"""
Задание 4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгон до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавка')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворот {direction}')
        else:
            print('Не можем повернуть - мы стоим')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(
        f"Тест-драйв {'полицейский' if vehicle.is_police else 'гражданский'} авто {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('направо')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("Тест-драйв окончен", end="\n\n")


car = Car('белый', 'Lada vesta', False)
test_drive(car)

solaris = TownCar('красный', 'Hyundai Solaris', False)
test_drive(solaris)

lamba = SportCar('желтый', 'Lamborghini Huracán', False)
test_drive(lamba)

gaz = WorkCar('зеленый', 'ГАЗель Next', False)
test_drive(gaz)

corolla = PoliceCar('синий', 'Toyota Corolla', True)
test_drive(corolla)
