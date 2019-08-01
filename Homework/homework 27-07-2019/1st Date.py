import calendar


month = 11
year = 2012
day = calendar.day_name[1]

while True:
    if calendar.weekday(year, month, 1) == day:
        print(day)
        break
    if month == 13:
        month = 1
        year += 1
