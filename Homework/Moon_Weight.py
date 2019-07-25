from sys import stdin

print('Введите ваш земной вес: ')
weight = int(stdin.readline())
print('Введите ежегодный прирост вашего веса: ')
n = int(stdin.readline())
print('Введите колличество лет: ')
years = int(stdin.readline())


def moon(weight, n, years):
    moon_weight = 0
    for i in range(1, years + 1):
        moon_weight = weight * n
        weight += 1
        a = str('Год: ' + str(i) + ' Земной вес: ' + str(weight) + ' Лунный вес: ' + str(moon_weight))
        yield a


n = moon(weight, n, years)
for i in n:
    print(i)
