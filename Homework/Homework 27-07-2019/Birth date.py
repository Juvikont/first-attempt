from sys import stdin
import calendar

print('Введите дату рождения: ')
date = stdin.readline()
a = date.split('.')
day = int(a[0])
month = int(a[1])
year = int(a[2])

x = calendar.weekday(year, month, day)
print(list(calendar.day_name)[x])
