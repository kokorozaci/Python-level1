# Задание 2

time_sec = int(input('Введите время в секундах\n'))
mm = time_sec%60**2
print(time_sec//60**2, mm//60, mm%60, sep=':')
# или так
hh = time_sec//60**2
ss = mm%60
print(f'{hh}:{mm//60}:{ss}')
# если нужен формат 02:02:02
if hh <= 9:
    hh = f'0{hh}'
if mm//60 <= 9:
    mm = f'0{mm//60}'
else:
    mm = mm//60
if ss <= 9:
    ss = f'0{ss}'
print(f'{hh}:{mm}:{ss}')