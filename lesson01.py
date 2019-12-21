# Задание 1

name = 'Anna'
age = 31
print(f'Привет, меня зовут {name}, мне {age} год.')
user_name = input('А как тебя зовут?\n-> ')
age = input(f'Привет, {user_name}, сколько тебе лет?\n-> ')
city = 'Санкт-Петербурге'
print(f'Я живу в {city}')
user_city = input('Где ты жвёшь?\n-> ')
x = input('Назови любое число\n-> ')
print('-'*50)
print(f'Тебя зовут {user_name}, тебе {age}, ты живёшь {user_city}. Число {x}')

# Задание 2

time_sec = int(input('Введите время в секундах\n'))
mm = time_sec%60**2
print(time_sec//60**2, mm//60, mm%60, sep=':')
# или так
hh = time_sec//60**2
ss = mm%60
print(f'{hh}:{mm//60}:{ss}')
# если нужен формат 02:02:02
# if hh <= 9:
#     hh = f'0{hh}'
# if mm//60 <= 9:
#     mm = f'0{mm//60}'
# else:
#     mm = mm//60
# if ss <= 9:
#     ss = f'0{ss}'
# print(f'{hh}:{mm}:{ss}')
# идеальный вариант
mm = (time_sec%60**2)//60
print(f'{hh:02}:{mm:02}:{ss:02}')

# Задание 3

n = input('Введите число\n')
if n[0] == '-':
    n = n[1:]
print(int(n)+int(f'{n}{n}')+int(f'{n}{n}{n}'))
# Или может так
n = int(input('Введите число\n'))
if n < 0:
    n = n*(-1)
print(n + int(f'{n}{n}') + int(f'{n}{n}{n}'))
# ещё лучше
n = input('Введите число\n')
print(f'{int(n) + int(n+n) + int(n+n+n)}')

# Задание 4

number = int(input('Введите целое положительное число\n'))
x = 0
while number > 0:
    x = number%10 if x < number%10 else x
    number = number//10
print(x)

# Задание 5

income = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
value = income - costs
if value > 0:
    print(f'Прибыль: {value}')
    rent = income/costs
    print(f'Рентабильность: {rent}')
    staff = int((input('Введите число сотрудников: ')))
    value_to_staff = rent/staff
    print(f'Прибыль на 1 сотрудника: {value_to_staff}')
elif value < 0:
    print(f'Убыток: {value}')
else: print('Поздравляю, вы работаете в 0 (=')

# Задание 6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.

a = int(input('В 1-й день дистанция (в км): '))
b = int(input('Цель (в км): '))
day = 1
print(f'{day}-й день: {round(a, 2)}')
while a <= b:
    day += 1
    a = a * 1.1
    print(f'{day}-й день: {round(a, 2)}')
print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {int(a//1)} км.')
