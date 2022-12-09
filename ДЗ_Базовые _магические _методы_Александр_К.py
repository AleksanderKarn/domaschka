### Задание 1. Метод __call__
import math


class Derivative:
    def __init__(self, funk):
        self.__funk = funk

    def __call__(self, *args: object, **kwargs: object) -> object:
        return math.cos(self.__funk(*args, **kwargs))


@Derivative
def sin_(x):
    return math.sin(x)


# print(sin_(math.pi/3))


### Задание 2. Метод __str__

class Flight:

    def __init__(self, city_from, city_to):
        self.__city_from = city_from
        self.__city_to = city_to

    def __str__(self):
        return f'Flight from {self.__city_from} to {self.__city_to}'


# print(Flight(input(), input()))

### Задание 3. Магические методы арифметических выражений и ### Задание 4. Сравнения

class MyInt:
    def __init__(self, val):
        self.__val = val

    def __str__(self):
        return str(self.__val)

    def __repr__(self):
        return f'{self.__class__}:{self.__val}'

    @classmethod
    def check_str(cls, other):
        if isinstance(other, str):
            return int(other)
        return other

    def __add__(self, other):
        oth = self.check_str(other)
        return MyInt(self.__val + oth)

    def __sub__(self, other):
        oth = self.check_str(other)
        return MyInt(self.__val - oth)

    def __mul__(self, other):
        oth = self.check_str(other)
        return MyInt(self.__val * oth)

    def __truediv__(self, other):
        oth = self.check_str(other)
        return MyInt(self.__val / oth)

    def __eq__(self, other):
        oth = self.check_str(other)
        return self.__val == oth

    def __lt__(self, other):
        oth = self.check_str(other)
        return self.__val < oth

    def __getnewargs__(self, other):
        oth = self.check_str(other)
        return self.__val >= oth

    def __gt__(self, other):
        oth = self.check_str(other)
        return self.__val > oth

    def __le__(self, other):
        oth = self.check_str(other)
        return self.__val <= oth

    def __ge__(self, other):
        oth = self.check_str(other)
        return self.__val >= oth


a = MyInt(5)
a = a + 5
print(a)
a = a - 2 - 3
print(a)
a = a * '5'
print(a)
a = a / 10
print(a)
print(type(a))
b = '24'
print(a >= b)
print(a <= b)
print(a == b)
print(a > b)
print(a < b)
print(a != b)
b = 56
print(a >= b)
print(a <= b)
print(a == b)
print(a > b)
print(a < b)
print(a != b)
