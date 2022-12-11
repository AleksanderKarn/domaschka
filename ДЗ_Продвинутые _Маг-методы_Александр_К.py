### Продвинутые магические методы. Домашнее задание

### Задание 1. Метод __hash__
import datetime


class Task:

    def __init__(self, content):
        self.content = content
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M")
        self.date = date

    def __keys(self):
        return f'{self.content} (создано {self.date})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other
        return NotImplementedError

    def __hash__(self):
        return hash(self.content)

    def __repr__(self):
        return str(self.__keys())

    ### Задание 2. Метод __bool__

    def __bool__(self):
        return bool(self.content)


# todo_list = set()
# todo_list.add(Task('Сделать домашку'))
# todo_list.add(Task('Выпить кофе'))
# todo_list.add(Task('Выйти на пробежку'))
# todo_list.add(Task('Сделать домашку'))
# for item in todo_list:
#    print(item)


### Задание 2. Метод __bool__ ###
# todo_list = []
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
#
# non_empty_tasks = [item for item in todo_list if item]
# print(non_empty_tasks)
# print(len([item for item in todo_list if not item]))


###Задание 3. Метод __getitem__ и __setitem__### и Задание 4. Метод __next__


class TodoList:

    def __init__(self):
        self.tasks = [None] * 2
        self.__step = -1

    def __setitem__(self, key, value):
        self.tasks[key] = value

    def __repr__(self):
        return str(self.tasks)

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __next__(self):

        self.__step += 1
        if len(self.tasks) > self.__step:
            return self.tasks[self.__step]
        else:
            raise StopIteration

    def __iter__(self):
        self.__step = -1
        return self


todo_list = TodoList()
# print(todo_list.tasks)
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
# todo_list[0] = Task('Сдать домашку')
# print(todo_list)
# print(type(Task('Сдать домашку')))
# print(todo_list[1])

# del todo_list[0]
# print(todo_list)

# print(next(todo_list))
# print(next(todo_list))
# print(next(todo_list))
# next(todo_list)
for item in todo_list: print(item)
