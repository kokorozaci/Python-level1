import sys
def zp(hour, cash_in_hour, bonus):
    cash = (hour*cash_in_hour) + bonus
    return cash

if __name__ == '__main__':
    params = sys.argv
    # print(params)
    if 'h' in params or 'help' in params:
        print('param 1: all work hour\nparam 2: payment per hour\nparam 3: bonus')
    else:
        all_hour = int(params[1])
        payment_per_hour = int(params[2])
        bonus = int(params[3])
        payment = zp(all_hour, payment_per_hour, bonus)
        print(f'Salary = {payment}')