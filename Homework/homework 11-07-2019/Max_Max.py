import random

a = int(input('Please provide the number: '))
x = []
for index in range(a):
    x.append(random.randint(10, 100))
print(x)
max1 = 0
max1_index = 0
max2 = 0
for index in range(len(x) - 1, 0, -1):
    if x[index] > max1:
        max1 = x[index]
        max1_index = index
del x[max1_index]
for index in range(len(x) - 1, 0, -1):
    if x[index] > max2:
        max2 = x[index]
print(max1, max2)
