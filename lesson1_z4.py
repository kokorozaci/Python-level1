# Задание 4
number = input('Введите целое положительное число\n')
n = len(number)
n_list = [int(i) for i in number]
n_max = max(n_list)
print(n_max)
# что-то у меня с математикой плохо -_-
# а если подумать...
number = int(input('Введите целое положительное число\n'))
x = 0
while number > 0:
    ost = number%10
    number = number//10
    if x < ost:
        x = ost
print(x)