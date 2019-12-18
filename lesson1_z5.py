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
