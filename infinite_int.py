from itertools import count

start = int(input('Введите число для старта: '))
for n in count(start, 1):
    print(n)