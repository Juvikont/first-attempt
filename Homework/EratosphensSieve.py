# number = int(input('Введите число: '))
# array = []
# prime_number = []
# for x in range(number):
#     array.append(x + 1)
# for i in range(2, len(array) - 1, 1):
#     value = array[i]
#     if value != i+1 and value % 2 == 0 and value % 3 == 0 and value % 5 == 0 and value % 7 == 0:
#         array[i] = 0
# print(array)

x = int(input('Введите число: '))
sieve = list(range(x + 1))
for i in sieve:
    if i > 1:
        for x in range(i + i, len(sieve), i):
            sieve[x] = 0
# comment
print(sieve)