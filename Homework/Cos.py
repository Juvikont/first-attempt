from math import cos

x = int(input('Please provide the number: '))
n = int(input('Please provide an N: '))


while n > 0:
    x = cos(x)
    n -= 1
print(x)
