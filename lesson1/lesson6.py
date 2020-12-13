import time

print('Task 1')
'''
1. Создать класс TrafficLight (светофор)
и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''


''' !
Последнее условие сформулировано неясно. Зачем проверять порядок режимов,
 если по условию их порядок должен быть вшит в один метод - running.
'''


class TrafficLight:
    __color = 'red'

    def running(self):
        timing = {'red': 7, 'yellow': 2, 'green': 7}  # Правильнее определить в атрибутах, но по условию - 1 атрибут
        order = ['red', 'yellow', 'green']
        order.remove(self.__color)  # остаются 2 других цвета
        order = order[::-1] if self.__color == 'yellow' else order
        print(self.__color)
        time.sleep(timing[self.__color])
        for color in order:
            print(color)
            time.sleep(timing[color])


traffic_light = TrafficLight()
traffic_light.running()

# Попробуем форсированно поменять цвет на желтый, а затем убедиться, что порядок сохранен
broken_t_light = TrafficLight()
broken_t_light._TrafficLight__color = 'yellow'
broken_t_light.running()

# Теперь проверим зеленый
broken_t_light._TrafficLight__color = 'green'
broken_t_light.running()

# => при данной реализации порядок сохранен при любом стартовом состоянии

print('Task 2')
'''
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

''' !
В данном задании также есть неточности.
1. Не указано, должна ли толщина задаваться пользователем или быть по умолчанию?
2. То же самое - 25 кг - откуда они берутся.

Решение сформировано исходя из предположения, что 1 - вшито по умолчанию, но
может задаваться и пользователем,
2 - вшито по умолчанию.'''


class Road:
    __kg_for_1_square_m = 25

    def __init__(self, length, width, thickness=5):
        self._length = length
        self._width = width
        self._thickness = thickness

    def get_mass(self):
        return f'{int(self._length * self._width * self.__kg_for_1_square_m * self._thickness / 1000)} т'  # в тоннах


road = Road(5000, 20)
print(road.get_mass())

print('Task 3')
'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income: dict):
        super(Position, self).__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return self._income["wage"] + self._income["bonus"]
        except KeyError:
            print('Ошибка. В качестве income нужно передать словарь вида {"wage": оклад, "bonus": бонус}')


position_test = Position('Cornelius', 'Fudge', 'minister', {"wage": 800000, "bonus": 100000})
print(position_test.get_full_name())
print(position_test.get_total_income())
print('Task 4')
'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = None

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction: str):
        self.direction = direction
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name, False)

    def favor_to_police(self, car: Car):
        if type(car) == SportCar:
            print('Полиция не сможет догнать эту машину. Придется ей помочь')
            self.is_police = True
        else:
            print('Полиция может справиться своими силами. Оставим спорткар гонщикам')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')
        if self.speed > 100:
            print('Превышение скорости')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)

    def catching_up(self, car: Car):
        self.go()
        print(f'Машина, {car.name} цвета {car.color}, это полиция! остановитесь!')
        self.speed = car.speed + car.speed * 0.3
        if car.direction is not None:
            self.turn(car.direction)

    def turn_if_criminal_turn(self, car: Car):
        print('Полиция повернула вслед за преступником')
        self.direction = car.direction


sport = SportCar(300, 'red', 'SportCar111')
print(sport.is_police)
print(sport.color)

criminal = SportCar(200, 'black', 'I_am_dangerous')
criminal.go()
criminal.show_speed()

sport.favor_to_police(criminal)
print(sport.is_police)

police = PoliceCar(sport.speed, sport.color, sport.name + '_police')
police.catching_up(criminal)
police.show_speed()

criminal.turn('Налево')
police.turn_if_criminal_turn(criminal)
print(police.direction)
print('Task 5')
'''
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 

Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 

Для каждого из классов методы должен выводить уникальное сообщение. 

Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super(Pen, self).__init__('pen')

    def draw(self):
        print('Ручка что-то написала')


class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__('pencil')

    def draw(self):
        print('Карандаш что-то начертил')


class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__('handle')

    def draw(self):
        print('Маркер поставил кляксу')


stationary = Stationery('Eraser')
stationary.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()


