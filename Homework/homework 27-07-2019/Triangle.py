import math as m

a = float(input('Введите A: '))
b = float(input('Введите В: '))
c = float(input('Введите С: '))

if (a + b >= c) and (b + c >= a) and (a + c >= b):
    print('Это треугольник! ')
    A = m.degrees(m.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    B = m.degrees(m.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a)))
    C = m.degrees(m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    print(A, B, C)
    print(int(A+B+C))
else:
    print('Это не треугольник! ')
