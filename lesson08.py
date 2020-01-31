""" Задание 1 """


class DateError(Exception):
    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        return 'Дата не существует'


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        date_split = cls(date).date.split('-')
        return tuple(map(int, date_split))

    @staticmethod
    def validation(date):
        a, b, c = Date.date_to_int(date)
        if not ((b == 2 and c%4 == 0 and a in range(1, 30)) or
                (b == 2 and c%4 != 0 and a in range(1, 29)) or
                (b in range(1, 13, 2) and a in range(1, 32)) or
                (b in range(4, 13, 2) and a in range(1, 31))):
            raise DateError()


print(Date.date_to_int('21-09-2019'))
try:
    Date.validation('31-12-2020')
except DateError as e:
    print(e)

""" Задание 2 """


class ZeroError(Exception):
    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        return 'деление на 0'


a = int(input('а: '))
try:
    b = int(input('b: '))
    if b == 0:
        raise ZeroError()
    else:
        print(a/b)
except ZeroError as e:
    print(e)


""" Задание 3 """

import re

class ElementNotNumber(Exception):
    def __init__(self, text=None):
        self.text = text
    def __str__(self):
        return 'Не число'

list_n = []
while True:
    el = input('Чтобы закончить введите "stop" \nВвод: ')
    if el == 'stop':
        break
    try:
        if re.search('[^\d.]', el):
            raise ElementNotNumber()
    except ElementNotNumber as e:
        print(e)
    else:
        list_n.append(float(el) if '.' in el else int(el))
print(list_n)

""" Задание 4,5 """

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.units = {}
        self.products = []

    def acceptance(self, product, amount):
        if product in self.products:
            


        if self.units[product.__class__.__name__]:
            self.units[product.__class__.__name__].append(product)
        else:
            self.units[product.__class__.__name__] = [product]

    def count_product(self):
        self.count_prod = {k: len(v) for k, v in self.units}

class OfficeEquipment:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

class Printer(OfficeEquipment):
    def __init__(self, price, brand, print_type, speed, color):
        super().__init__(price, brand)
        self.type_print = print_type
        self.speed_print = speed
        self.color_print = color

class Scanner(OfficeEquipment):
    def __init__(self, price, brand, dpi):
        super().__init__(price, brand)
        self.dpi = dpi

class Xerox(Printer, Scanner):
    pass


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата."""
#
#
