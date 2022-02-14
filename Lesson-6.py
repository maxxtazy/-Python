# Задание 1
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(10)
            i += 1


tl = TrafficLight()
tl.running()


# Задание 2
class Road:
    _length = None
    _width = None
    weight = None
    thickness = None

    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width

    def mass(self):
        self.weight = 25
        self.thickness = 0.05
        mass = self.length * self.width * self.weight * self.thickness
        print(f'Необходимо {mass} килограмм асфальта')


road = Road(5000, 20)
road.mass()

# Задание 3
class Worker:
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker = Position('Иван', 'Иванов', 'разработчик', 150000, 50000)
print(worker.name)
print(worker.surname)
print(worker.position)
print(worker._income)
print(worker.get_full_name(), worker.get_full_income())

# Задание 4
class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула ' + direction

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} - {self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} выше, чем разрешено в городе!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость грузового авто {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше, чем разрешено для грузового авто!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейский автомобиль'
        else:
            return f'{self.name} - это не полицейский автомобиль'


ferrari = SportCar(250, 'Красный', 'Ferrari', False)
kia = TownCar(80, 'Белый', 'KIA', False)
kamaz = WorkCar(70, 'Оранжевый', 'КАМАЗ', False)
lada = PoliceCar(110, 'Синий', 'Лада', True)
print(lada.turn('налево'))
print(lada.show_speed())
print(f'Цвет машины {lada.name} - {lada.color}')
print(f'{ferrari.name} полицейский авто? {ferrari.is_police}')
print(f'{lada.name} полицейский авто? {lada.is_police}')
print(ferrari.show_speed())
print(kia.show_speed())
print(lada.police())
print(lada.show_speed())
print(kamaz.show_speed())

# Задание 5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
