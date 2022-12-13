### # Наследование. Домашнее задание

## Задание 1. Функции issubclass() и isinstance()
class Item:
    def __init__(self, name, price, quantity=0):
        # self.__check(name, price, quantity)

        self.name = name
        self.price = price
        self.quantity = quantity

    def __check(self, name, price, quantity):
        if not isinstance(name, str):
            raise print(f'TypeError: Название товара должно быть строкой.')
        if not isinstance(price, (int, float)):
            raise print(f'TypeError: Цена товара должна быть числом.')
        if not isinstance(quantity, int):
            raise print(f'TypeError: Количество товара должно быть целым числом.')

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'


# print(Item('phone', 18000, 5))

# print(Item(18000, 'phone', 5))
# print(Item('phone', '18000', 5))
# print(Item('phone', 18000, 5.5))


### Задание 2. Функция super()

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        self.broken_phones = broken_phones
        super().__init__(name, price, quantity)

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}),{self.broken_phones}'


phone1 = Phone("iPhone 10", 500, 5, 2)


# print(phone1)

### Задание 3. Логер магических методов ###


class MyList(list):

    def __new__(cls, *args, **kwargs):
        print(f'Работает магический метод __new__')
        return super().__new__(cls)

    def __init__(self, lst_1):
        print(f'Работает магический метод __init__')
        self.name = lst_1[0]
        self.surname = lst_1[1]
        self.language = lst_1[2]
        self.lst_1 = lst_1

    def __str__(self):
        print((f'Работает магический метод __str__'))
        return str(self.lst_1)

    def __len__(self):
        print(f'Работает магический метод __len__')
        return len(self.lst_1)

    def __getitem__(self, item):
        print(f'Работает магический метод __getitem__')
        return self.lst_1[item]

    def __setitem__(self, key, value):
        print(f'Работает магический метод __setitem__')
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        self.lst_1[key] = value


# lst = MyList(['Jone', 'Snow', 'Java'])

# if not lst[2] == 'Python':
#    lst[2] = 'Python'

# print(lst)
# print(len(lst))


### Задание 4. Private атрибуты при наследовании ###

class TeamIterator:

    def __init__(self, team):
        self.count = 0
        self.value = team

    def __next__(self):
        if self.count < (len(self.value._juniorMembers) + len(self.value._seniorMembers)):
            if self.count < len(self.value._juniorMembers):
                result = (self.value._juniorMembers[self.count], 'junior')
            else:
                result = (self.value._seniorMembers[self.count - len(self.value._juniorMembers)], 'senior')

            self.count += 1
            return result
        raise StopIteration


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
