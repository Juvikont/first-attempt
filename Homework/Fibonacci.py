# n = int(input('Введите число: '))
# fib = [0, 1]
# index = 2
# while fib[len(fib) - 1] <= n:
#     fib.append(fib[index - 1] + fib[index - 2])
#     index += 1
# if fib[len(fib) - 1] >= n:
#     del fib[len(fib) - 1]
# print(fib)

# n = int(input('Введите число: '))
# fib = [0, 1]
# for y in range(n):
#     if y >= 2:
#         number = fib[y - 1] + fib[y - 2]
#         if number <= n:
#             fib.append(number)
#         else:
#             break
# print(fib)

n = int(input('Введите число: '))
fib = [0, 1]
for y in range(n):
    final_number = list(*map(lambda x: fib[y-1]+ fib[y-2],fib))
print(fib)




# def f():
#     x = 1
#     y = 1
#     yield x
#     yield y
#     n=0
#     while n<10:
#         x, y = y, x + y
#         n+=1
#         yield y
#
#
# i = 0
# for i in f():
#     print(i)