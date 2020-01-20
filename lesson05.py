# # Задание 1

with open('lesson05/text1.txt', 'w') as f:
    while True:
        text = input('Напечатайте что-нибудь: ')
        if not text:
            break
        f.write(f'{text}\n')


# Задание 2

def to_list(s):
    if '\n' in s:
        s = s[:-1]
    s = s.split()
    return len(s)


with open('lesson05/text2.txt', 'r', encoding='utf_8') as f:
    count_str = [to_list(line_n) for line_n in f.readlines()]
print(f'Строк в файле: {len(count_str)}')
print(f'Слов в каждой из строк: {count_str}')

# Задание 3

def zp(i):
    if '\n' in i:
        i = i[:-1]
    i = i.split()
    if float(i[1]) < 20000:
        print(f'Зарплата меньше 20 000 р. у {i[0]}а')
    return float(i[1])

with open('lesson05/text3.txt', 'r', encoding='utf-8') as f:
    zp_1 = [zp(lin) for lin in f.readlines()]
mean_zp = sum(zp_1) / len(zp_1)
print(f'Средняя зп сотрудников: {mean_zp:.02f}')

# Задание 4

dict_count = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
f2 = open('lesson05/text4_new.txt', 'w', encoding='utf-8')
with open('lesson05/text4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for l in lines:
        if '\n' in l:
            l = l[:-1]
        l = l.split()
        f2.write(f'{dict_count[l[0]]} — {l[-1]}\n')
f2.close()

# Задание 5

with open('lesson05/file5.txt', 'w+', encoding='utf-8') as f:
    numbers = [2, 5, 65, 8, 32, 59]
    for n in numbers:
        f.write(f'{n} ')
    f.seek(0)
    n_str = f.read()
    n_str = map(int, n_str.split())
    print(sum(n_str))

# Задание 6

import re

lessons = {}
with open('lesson05/text6.txt', 'r', encoding='utf-8') as f:
    for l in f.readlines():
        numbers = map(int, re.findall(r'\d{1,}', l))
        ns = l.split()[0]
        lessons[ns[:-1]] = sum(numbers)
print(lessons)

# Задание 7

import json

all_value = 0
i = 0
all_dict = [{}, {}]
with open('lesson05/text7.txt', 'r', encoding='utf_8') as f:
    for line in f.readlines():
        firm = line.split()
        value = int(firm[2]) - int(firm[3])
        all_dict[0][firm[0]] = value
        if value > 0:
            all_value += value
            i += 1
    all_dict[1]['avarage_profit'] = all_value / i
with open('lesson05/7.json', 'w') as f:
    json.dump(all_dict, f)
