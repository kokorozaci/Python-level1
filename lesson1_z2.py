# Задание 2
time_sec = int(input('Введите время в секундах\n'))
hour = time_sec//(60*60)
minites = time_sec//60
sec = time_sec - minites*60 - hour*60
print(hour, minites, sec, sep=':')
# или так
print(f'{hour}:{minites}:{sec}')