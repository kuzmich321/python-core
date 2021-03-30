from datetime import datetime, timezone
from fractions import Fraction
from math import sqrt
from functools import total_ordering


def my_dec(a, b):
    def decorator(fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={a}, b={b}')
            return fn(*args, **kwargs)
        return inner
    return decorator


@my_dec(10, 20)
def my_func(s):
    print(f'Hello {s}')


my_func('World')


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print(f'called a={self.a}, b={self.b}, c={c}')


obj = MyClass(10, 20)
obj(100)


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={self.a}, b={self.b}')
            return fn(*args, **kwargs)
        return inner


@MyClass(15, 25)
def my_func(s):
    print(f'Hello {s}')


my_func('World')
print('----------------')


f = Fraction(2)
print(f.numerator)
print(f.denominator)


Fraction.speak = 100
print(f.speak)

Fraction.speak = lambda self, message: f'Fraction says: {message}'
print(f.speak('This is a late parrot'))


f2 = Fraction(10, 5)
print(f2.speak('This parrot is no more'))


Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2, 3)
f2 = Fraction(64, 8)


print(f1.is_integral())
print(f2.is_integral())


def dec_speak(cls):
    cls.speak = lambda self, message: f'{self.__class__} says: {message}'
    return cls


Fraction = dec_speak(Fraction)
f1 = Fraction(2, 3)
print(f1.speak('hello'))


class Person:
    pass


Person = dec_speak(Person)
p = Person()
print(p.speak('this works'))
print('----------------')


def info(self):
    results = []
    results.append(f'time: {datetime.now(timezone.utc)}')
    results.append(f'Class: {self.__class__.__name__}')
    results.append(f'id: {hex(id(self))}')
    for k, v in vars(self).items():
        results.append(f'{k}: {v}')
    return results


def debug_info(cls):
    cls.debug = info
    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi(self):
        return 'Hello there!'


p = Person('John', 1939)
print(p.debug())


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed.')
        self._speed = new_speed


favorite = Automobile('Ford', 'Model T', 1908, 45)
print(favorite.debug())
# favorite.speed = 100
favorite.speed = 40
print(favorite.debug())
print('----------------')


def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls


@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        return NotImplemented


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)
print(p1)
print(p1 is p2)
print(p1 == p2)

p4 = Point(100, 100)
print(p1 < p4)
print(p2 >= p1)
print('----------------')


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        return NotImplemented


p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 100)
print(p1 > p2)
print(p1 <= p2)
print(p1 == p2)
print(p4 > p3)
