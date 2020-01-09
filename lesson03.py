# Задание 1

def del_a_b(a, b):
  return a/b

a = int(input('Веедите a (делимое): '))
b = int(input('Веедите b (делитель): '))
try:
  print(f'{a} / {b} = {del_a_b(a, b)}')
except ZeroDivisionError:
  print('Деление на 0')

# Задание 2

def user_info(**kwargs):
  for i, j in kwargs.items():
    print(f'{i}: {j}', end='; ')
# вар 2
def user_info_2(**kwargs):
    print(f'{kwargs.get("name")} {kwargs.get("surname")}, {kwargs.get("year")} г.р., '
          f'проживает в городе: {kwargs.get("city")}. E-mail: {kwargs.get("email")}; tel: {kwargs.get("phone_number")}')
# вар 3
def user_info_3(name='', surname='', year='', city='', email='', phone_number=''):
    print(f'{name} {surname}, {year} г.р., проживает в городе: {city}. E-mail: {email}; tel: {phone_number}')

name = input('Имя: ')
surname = input('Фамилия: ')
year = input('Год рождения: ')
city =  input('Город: ')
email = input('Емейл: ')
tel = input('Телефон: ')
user_info_3(name=name, surname=surname, year=year, city=city, email=email, phone_number=tel)

# Задание 3

def my_func(a, b, c):
  abc = sorted([a, b, c])
  return sum(abc[1:])
a = int(input('Число a: '))
b = int(input('Число b: '))
c = int(input('Число c: '))
summ = my_func(a, b, c)
print(f'Сумма 2-х наибольших чисел: {summ}')

# Заданеи 4

a = float(input('Введите действительное число: '))
n = int(input('Введите отрицательное целое число - степень: '))
def my_func(x, y):
    return x**y
print(my_func(a, n))
def my_func(x, y):
    b=x
    for i in range(y, -1):
        b = b*x
    return 1/b
print(my_func(a, n))

# Задание 5

def new_sum(sum_x=0):
    x = input('Введите числа через пробел\nДля завершения введите QQ\n: ').upper().split()
    if 'QQ' in x:
        sum_x = sum_x + sum(map(int, x[:x.index('QQ')]))
        return sum_x, True
    else:
        sum_x = sum_x + sum(map(int, x))
        return sum_x, False

y = 0
while True:
    try:
        y, qq = new_sum(y)
        print(f'Новая сумма: {y}\nКонец программы' if qq else f'Новая сумма: {y}')
        if qq:
            break
    except ValueError:
        print('Неверный ввод')

# Задание 6

def int_func(text):
  return text.title()

def new_func(text):
  x = map(int_func, text.split())
  x = ' '.join(x)
  return x

text = input('Введите слова через пробел\n: ')
print(new_func(text))