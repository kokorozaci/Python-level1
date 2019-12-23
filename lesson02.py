# Задание 1

my_list = [123, 'Hello', {2, 8, 6}, (2, 3), 523.35, None, {'name': 'Ann'}, 52, 'foo']
for el in my_list:
    print(type(el))

# Задание 2

u_list = []
while True:
    n = input('Введите элемент списка (закончить список: ENTERN)\n: ')
    if n == '':
        break
    u_list.append(n)
new_list = []
for i in range(0, len(u_list), 2):
    new_list.append(u_list[i+1] if i+1 != len(u_list) else u_list[i])
    new_list.append(u_list[i]) if i+1 != len(u_list) else new_list
print(new_list)
# var 2
for i in range(1, len(u_list), 2):
    u_list[i-1], u_list[i] = u_list[i], u_list[i-1]
print(u_list)

# Задание 3

while True:
    try:
        month = int(input('Введите месяц (формат: 1, 2, и т.д.)\n: '))
        if month >= 1 and month <= 12:
            break
        else:
            print('Месяц должен быть от 1 до 12')
    except ValueError:
        print('Неверный формат')

# Вариант со словарём
months = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for key, m in months.items():
    if month in m:
        print(key)
        break
#
# Вариант с листом
months_1 = ['', 'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
print(months_1[month])

# Задание 4

my_str = input('Введите несколько слов через пробел\n: ')
words = my_str.split()
for i, word in enumerate(words, start=1):
    print(i, word if len(word) <=10 else word[:10])

# # Задание 5

my_list = [7, 5, 3, 3, 2]
new_number = int(input('Введите целое натуральное число\n--> '))
my_list.append(new_number)
print(sorted(my_list, reverse=True))
# var 2
for el in my_list[:]:
    if new_number > el:
        my_list.insert(my_list.index(el), new_number)
        break
    elif new_number < my_list[-1]:
        my_list.append(new_number)
        break
print(my_list)

# Задание 6

n_good = 1
goods = []
next_g = 'н'
while next_g != 'д':
    name_g = input('название: ')
    price_g = float(input('цена: '))
    count_g = int(input('кол-во: '))
    mesur_g = input('ед. измерения: ')
    good = (n_good, {'название': name_g, 'цена': price_g, 'количество': count_g, 'ед': mesur_g})
    goods.append(good)
    next_g = input('Закончить ввод? д/н: ')
    n_good += 1
print(goods)
new_dict = {}
for g in goods:
    for key_g, value_g in g[1].items():
        if key_g in new_dict:
            new_dict[key_g].append(value_g)
        else:
            new_dict[key_g] = [value_g]
print(new_dict)