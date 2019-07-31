from random import randint as r
from sys import stdin as st
from functools import reduce as re

print('Сколько чисел вы хотите обработать? ')
num = int(st.readline())
x = []
for index in range(num):
    x.append(r(1, 9))
print(x)
print('Введите операцию: ')
method = input()
splitted_method = method.split(' ')
last = splitted_method[0]
middle = splitted_method[1]
first = splitted_method[2]

filters = {'sum': re((lambda c, d: c + d), x),
           'multiply': re((lambda c, d: c * d), x),
           'join': re((lambda c, d: str(c) + str(d)), x),
           'reverse': x[::-1],
           'unite': list(set(x[:])),

           'negated': list(map(lambda c: c * -1, x)),
           'inverted': list(map(lambda c: 1 / c, x)),
           'squared': list(map(lambda c: c ** 2, x)),

           'odds': list(filter(lambda c: c % 2 != 0, x)),
           'evens': list(filter(lambda c: c % 2 == 0, x)),
           'simples': list(filter(lambda c: c % 2 == 0, x)),
           'primes': list(filter(lambda c: c in (1, 3, 5, 7), x))
           }


expression = (re((lambda c: filters[first],filters[middle],filters[last])),x)
print(expression)