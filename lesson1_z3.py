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
