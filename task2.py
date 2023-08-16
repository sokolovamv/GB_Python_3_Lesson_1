number = int(input('Введите число от 0 до 100000: '))
if number > 2 and number < 100001:
    for i in range(2, number):
        if number % i == 0:
            print(f'Число {number} составное')
            break
        elif i == number - 1:
            print(f'Число {number} простое')
        else:
            continue
elif number == 2:
    print(f'Число {number} простое')
elif number == 0 or number == 1:
    print(f'Число {number} не является ни простым, ни составным')
else:
    print('Вы ввели число вне предоставленного диапазона')