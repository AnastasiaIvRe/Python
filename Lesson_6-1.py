"""
Задание 1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (
запуск); атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный,
жёлтый, зелёный; продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод.

"""

from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle([
        {'signal': 'red', 'duration': 7},
        {'signal': 'yellow', 'duration': 2},
        {'signal': 'green', 'duration': 4},
        {'signal': 'yellow', 'duration': 2}
    ])

    def running(self):
        light = next(self.__color)
        print(f"Сигнал {light['signal']}, пауза {light['duration']} сек.")
        sleep(light['duration'])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
