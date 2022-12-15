### Задание 1. Простая функция

def calc_salt(m):
    salt = 10
    if isinstance(m, str):
        try:
            if isinstance(int(m), int):
                res = int(m) / 1000 * salt
        except ValueError:
            print(f"invalid literal for int() with base 10: '{m}'")
            return 0.0
    else:
        res = m / 1000 * salt
    return res


print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))
print('*' * 30)
### Задание 2. Все блоки try ###

import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        doc = open(file)
    except FileNotFoundError as error:
        print(error)
        print(f'Time required for {file} = 0.0')

    else:
        result = doc.read()
        end_time = time.time()
        t = end_time - start_time
        t_str = f'Time required for {file} = {t}'
        return result, t_str

    finally:
        print('содержимое файла прочитано')


### Задание 3. InvalidAgeError ###


class InvalidAgeError(Exception):
    def __init__(self, *args):
        if args:
            self.str = args[0]

    def __str__(self):
        if self.str:
            return self.str


try:
    age = int(input('Введите ваш возраст: '))
    if age < 0 or age >= 120:
        raise InvalidAgeError('Извините, этот возраст не корректен')
    print(f'Вам {age} лет')
except ValueError:
    print('Возраст должен быть числом')
except InvalidAgeError as e:
    print(e)

print('*' * 30)
### Задание 4. Класс Item ###

import csv


class Item:
    pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file, newline='') as csvf:
            res = csv.DictReader(csvf)
            for row in res:
                item_1 = Item(row['name'], row['price'], row['quantity'])
                Item.all.append(item_1)

    def __str__(self):
        return f"Item('{self.name}', {float(self.price)}, {self.quantity})"


Item.instantiate_from_csv('items.csv')

for item in Item.all:
    print(item)
    
print('*' * 30)