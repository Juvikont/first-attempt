import random

a = int(input('Введите сколько чисел вы хотите сравнить: '))
x = []
for index in range(a):
    x.append(random.randint(25, 1000))
print(x)
min = x[0]
max = 0
for index in range(len(x) - 1, 0, -1):
        if x[index] < min:
            min = x[index]
        elif x[index] > max:
            max = x[index]

print(min, max)
