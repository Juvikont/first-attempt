from random import randint as r
from sys import stdin as st

x = (r(0, 10))
while True:

    print('Введите число: ')
    a = st.readline()
    if x == int(a):
        print('Вы угадали! ')
        break
    else:
        print('Graj dalej kurwa! ')
