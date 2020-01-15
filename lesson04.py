import random as rd
from functools import reduce

# Задание 1
# см. zp_lesson04.py

# Задание 2
numbers = [rd.randint(0, 100) for i in range(20)]  # исходный список
print(numbers)
new_list = [numbers[i] for i in range(len(numbers)) if numbers[i] > numbers[i-1]]
print(new_list)

# Задание 3
list_numbers = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]
print(list_numbers)
# а если уж совсем в 1 строку
[print(n, end='  ') for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]

# Задание 4
numbers = [rd.randint(0, 20) for i in range(20)]  # исходный список
print('\n', numbers)
new = [n for n in numbers if numbers.count(n) == 1]
print(new)

# Задание 5

new = [n for n in range(100, 1001) if n % 2 == 0]
print(reduce(lambda x, y: x*y, new))

# Задание 6

def fibo_gen(stop):
    x = 1
    for n in range(1, stop):
        x *= n
        yield x

for n in fibo_gen(15):
    print(n)
