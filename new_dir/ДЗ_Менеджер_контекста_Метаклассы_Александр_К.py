### Задание 1. Менеджер контекста ###

import os


class ChangeDir:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


# with ChangeDir('dir1'):
#    print(os.listdir())
#
# with ChangeDir('dir2'):
#    print(os.listdir())


### Задание 2.  ###

class ReadItems:

    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        lis = []
        items = []
        self.dic = open(self.file)
        for i in self.dic:
            lis.append(i.split(','))
        for j in range(len(lis)):
            a = lis[0][0]
            b = lis[0][1]
            c = lis[0][2].replace('\n','')
            x = lis[j][0].replace('"','')
            y = lis[j][1]
            z = lis[j][2].replace('\n','')
            items.append({a: x, b: y, c: z})
        items = items[1:]
        return items

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dic.close()


def show_items(file):
    with ReadItems(file, 'r') as items:
        for item in items:
            print(item)


#show_items('items.csv')


### Задание 3. Вложенный класс ###


class Student:

    def __init__(self, name, stud_id):
        self.name = name
        self.student_id = stud_id
        self.lap = self.Laptop()

    def show(self):
        """Вывести информацию о студенте и его ноутбуке"""
        return f'{self.name} {self.student_id}\n{self.lap.brand} {self.lap.cpu} {self.lap.ram}'

    class Laptop:

        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = '8'




s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)
print('*'* 30)
print(s1.show())
print('*'* 30)
s1.lap.ram = 16
print(s1.show())
print('*'* 30)
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))
print('*'* 30)

### Задание 4*. Динамическое создание класса ###





