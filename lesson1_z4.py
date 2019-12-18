# Задание 4

number = int(input('Введите целое положительное число\n'))
x = 0
while number > 0:
    x = number%10 if x < number%10 else x
    number = number//10
print(x)