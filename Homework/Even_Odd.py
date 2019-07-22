import random

a = int(input('Колличество числел: '))
x = []
final = []
for index in range(a):
    x.append(random.randint(25, 1000))
for index in range(len(x) - 1, 0, -1):
    if x[index] % 2 == 0:
        final.insert(0, x[index])
    else:
        final.append(x[index])
print(final)
