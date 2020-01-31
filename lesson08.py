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

""" Задание 4,5,6 """

class Warehouse:
    def __init__(self, units):
        self.units = {unit: [] for unit in units}
        self.sort_p = {}
        self.products = []

    def acceptance(self, product, amount):
        try:
            if type(amount) != int:
                raise ValueError('Только целое число')
        except ValueError as e:
            print(e)
        self.products.append({product: amount})

    def sort_units(self):  # если считать что подразделения занимаются каждое свом видом оргтехники
        for prod in self.products:
            for k, v in prod.items():
                if self.sort_p[k]:
                    self.sort_p[k] += v
                else:
                    self.sort_p[k] = v

    def rebase(self, obj, unit):  # сортировка вручную
        self.units[unit].append(obj)

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

""" Задание 7 """

class ComplexNum:
    """ a + b i """
    def __init__(self, a, b):
        self.num = (a, b)

    def __str__(self):
        if self.num[1] >= 0:
            if self.num[0] == 0:
                return f'{self.num[1]}i'
            else:
                return f'{self.num[0]}+{self.num[1]}i'
        elif self.num[1] < 0:
            if self.num[0] == 0:
                return f'{self.num[1]}i'
            else:
                return f'{self.num[0]}{self.num[1]}i'

    def __mul__(self, other):
        new_a, new_b = self.num[0]*other.num[0]-self.num[1]*other.num[1], \
                       self.num[0]*other.num[1]+self.num[1]*other.num[0]
        return ComplexNum(new_a, new_b)

    def __add__(self, other):
        new_a, new_b = self.num[0] + other.num[0], \
                       self.num[1] + other.num[1]
        return ComplexNum(new_a, new_b)

n1 = ComplexNum(0, -3)
n2 = ComplexNum(5, 0)
print(n1)
print(n2)
print(n1*n2)
print((2-3j)*(5+1j))
print(n1+n2)
print((2-3j)+(5+1j))
