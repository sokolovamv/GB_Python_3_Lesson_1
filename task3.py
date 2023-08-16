from random import randint

lower_limit = 0
upper_limit = 1000
rand_num = randint(lower_limit,upper_limit)
attempts = 10
attempt = 0
while attempt < attempts:
    user_num = int(input(f'Введите число от {lower_limit} до {upper_limit})'))
    if user_num > rand_num:
        print('Введите число меньше')
        upper_limit = user_num
    elif user_num < rand_num:
        print('Введите число больше')
        lower_limit = user_num
    else:
        print('Вы угадали число')
        break
    attempt += 1
else:
    print('Вы не угадали число')