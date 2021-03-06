""" Задание 1 """

import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def runing(self, color):
        if color == 'red' and (self.__color == 'green' or self.__color is None):
            self.__color = color
            print('Red ...')
            time.sleep(7)
        elif color == 'yellow' and self.__color == 'red':
            self.__color = color
            print('Yellow ...')
            time.sleep(2)
        elif color == 'green' and self.__color == 'yellow':
            self.__color = color
            print('Green ...')
            time.sleep(5)
        else:
            raise Exception('Неверная последовательность сигналов')
            # print('Ошибка последовательности')

light = TrafficLight()
light.runing('red')
light.runing('yellow')
light.runing('green')
try:
    light.runing('yellow')
except Exception as e:
    print(e)

""" Задание 2 """

class Road:
    def __init__(self, lenght, widh):
        self._length = lenght
        self._width = widh

    def mass_asfalt(self, mass = 25, cm = 5):
        return self._length*self._length*mass*cm/1000

road = Road(20, 5000)
print(f'Масса асфальта: {road.mass_asfalt(30, 6)} т.')

""" Задание 3 """

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position('Иван', 'Иванов', 'директор', 250000, 20000)
print(position.position)
print(position.get_full_name())
print(position.get_total_income())

""" Задание 4 """

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def go(self):
        print('Car runing...')
    def stop(self):
        print('Car stop')
    def turn(self, direction):
        print(f'Car turn {direction}')
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._speed_limit = 60
    def show_speed(self):
        if self.speed > self._speed_limit:
            print('Превышение скорости')
        else:
            print(self.speed)

class SportCar(Car):
    pass
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._speed_limit = 40
    def show_speed(self):
        if self.speed > self._speed_limit:
            print('Превышение скорости')
        else:
            print(self.speed)
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def inspection(self, car):
        if car._speed_limit:
            if car.speed > car._speed_limit:
                print('Остоновитесь, Вы превысили скорость ...')

sport = SportCar(90, 'red', 'ferrari')
police = PoliceCar(120, 'blue', 'police')
work = WorkCar(40, 'yellow', 'трактор')
town = TownCar(70, 'green', 'renoult')
police.inspection(town)
town.go()
town.turn('left')
town.stop()
town.show_speed()
work.show_speed()
sport.show_speed()
police.show_speed()
print(police.is_police)
print(town.is_police)

""" Задание 5 """

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Запись.')
class Pencil(Stationery):
    def draw(self):
        print('Рисование.')
class Handle(Stationery):
    def draw(self):
        print('Расскраска.')

stationery = Stationery('1')
pen = Pen('Blue')
pencil = Pencil('B3')
handle = Handle('Красный маркер')
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
print(handle.title)

""" Дополнительно. Хотела проверить как ведёт себя метод 
который активируется в __init__ и как его выключить"""

class ListGenerator:
    def __init__(self):
        self.list = []
        self.add_tolist()
        print(f'Проверка списка  {self.list}')

    def add_tolist(self):
        self.list = [i*2 for i in range(25)]

class NullList(ListGenerator):
    def add_tolist(self):
        pass

null = NullList()
print(null.list)
full = ListGenerator()
print(full.list)