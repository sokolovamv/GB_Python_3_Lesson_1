a, b, c = int(input('Введите сторону a = ')), int(input('Введите сторону b = ')), int(input('Введите сторону c = '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b != c or a != b == c or b == c != a:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника не существует')