### Задание 1 Mixins###

class Vehicle:

    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return

    def move_along(self, route):
        print("moving")


class MixCar:
    def __init__(self):
        super().__init__()

    def turn_on_radio(self, name):
        print(f'Playing {name}')


class Car(Vehicle, MixCar):
    pass


class Airplane(Vehicle):
    pass

car = Car((10, 20))
car.turn_on_radio('Moscow FM')


### Задание 2. Повышение производительности ###

#import timeit
#from functools import partial
#
#
#class Person:
#    def __init__(self, name: str, address: str, email: str):
#        self.name = name
#        self.address = address
#        self.email = email
#
#
#class PersonTest:
#    __slots__ = ('name', 'address', 'email')
#
#    def __init__(self, name, address, email):
#        self.name = name
#        self.address = address
#        self.email = email
#
#
#def get_set_delete(person):
#    a = person.name
#    b = person.address
#    c = person.email
#    person.name = 'Alex'
#    person.address = 'Moscow'
#    person.email = 'USSR.RU'
#    del person
#
#
#def main():
#    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
#    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
#    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
#    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
#    print(f"Текущая реализация: {old}")
#    print(f"Тестовая реализация: {new}")
#    print(f"Улучшение производительности: {(old - new) / old:.2%}")
#
#
#if __name__ == "__main__":
#    main()
#
#
#### Задание 3. slots и property ###
#
#class Employee:
#    __slots__ = ('first', 'last')
#
#    def __init__(self, first, last):
#        self.first = first
#        self.last = last
#
#    @property
#    def email(self):
#        return f'{self.first}.{self.last}@email.com'
#
#    def get_fullname(self):
#        return f'{self.first} {self.last}'
#
#    def set_fullname(self, str):
#        a = str.split()
#        self.first = a[0]
#        self.last = a[1]
#
#    def del_fullname(self):
#        self.first = None
#        self.last = None
#
#    fullname = property(get_fullname, set_fullname, del_fullname)
#
#
#emp_1 = Employee('John', 'Smith')

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
# print('*'*20)
# emp_1.fullname = "Corey Schafer"
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
# print('*'*20)
# del emp_1.fullname
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
