""" Задание 1 """

class Matrix:
    def __init__(self, list_list):
        self.list = list_list
        self.str = ''

    def max_len_el(self):
        max_el = 0
        for l in self.list:
            max_el = max(l) if max_el<max(l) else max_el
        return len(str(max_el))

    def __str__(self):
        for l in self.list:
            self.str += ''.join([(str(j) + (self.max_len_el()-len(str(j))+1)*' ') for j in l]) + '\n'
        return self.str

    def __add__(self, other):
        assert len(self.list) == len(other.list)
        sum_m = []
        for i in range(len(self.list)):
            assert len(self.list[i]) == len(other.list[i])
            sum_m.append([(self.list[i][j]+other.list[i][j]) for j in range(len(self.list[i]))])
        return Matrix(sum_m)


m = Matrix([[1, 122, 8],[5, 3, 4]])
print(m)
n = Matrix([[2, 2, 81],[1, 1, 1]])
g = m + n
print(g)

""" Задание 2 """ # немного исправила, для личных нужд

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size, name):
        self._size = size
        self.name = name
        self._fabric_consumption = 0

    @abstractmethod
    def fabric_consumption(self):
        return round(self.size/6.5 + 0.5)

    @property
    def size(self):
        if self._size > 60:
            self._size = 60
        elif self._size < 40:
            self._size = 40
        elif self._size % 2 != 0:
            self._size += 1
        return self._size

class Dress(Clothes):
    def __init__(self, size, name, length = 100, len_sleeve = 0, incrimination = False):
        super().__init__(size, name)
        self.lenght = length
        self.len_sleeve = len_sleeve
        self.incrimination = incrimination

    def fabric_consumption(self):
        a = self.lenght/2 if self._size>52 else 0
        b = self.lenght/2 if self.incrimination else 0
        return round(self.lenght + a + self.len_sleeve/2 + b)

class Jumpsuit(Clothes):
    def __init__(self, size, name, height=165):
        super().__init__(size, name)
        self.height = height

    def fabric_consumption(self):
        a = self.height / 5 if self._size > 52 else 0
        return round(190 + a + 0.1*self.height)

c1 = Dress(40, 'Мара', 130, 10, False)
j1 = Jumpsuit(54, 'Марго')
print(c1.fabric_consumption())
print(j1.fabric_consumption())
print(j1.size)

""" Задание 3 """

class Cell:
    def __init__(self, cell_count=1):
        self.cell_count = cell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count > other.cell_count:
            return Cell(self.cell_count - other.cell_count)
        else:
            print('Получется меньше 1 клетки')

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(round(self.cell_count/other.cell_count))

    def make_order(self, n):
        str = ''
        for i in range(self.cell_count//n):
            str += '*'*n + '\n'
        if self.cell_count%n:
            str += '*'*(self.cell_count%n) + '.'*(n-self.cell_count%n)
        return str

cell = Cell(12)
cell2 = Cell(7)
cell3 = cell / cell2
cell4 = cell*cell2
print(cell4.make_order(20))