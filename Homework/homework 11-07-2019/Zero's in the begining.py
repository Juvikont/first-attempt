import random

n = int(input('Please provide the number: '))
# x = [1, 2, 5, 0, 17, 9, 0, 2, 0]
x = []
final = []
for index in range(n):
    x.append(random.randint(-1, 5))
for index in range(len(x) - 1, 0, -1):
    if x[index] == 0:
        final.append(0)
        del x[index]
print(final+x)
