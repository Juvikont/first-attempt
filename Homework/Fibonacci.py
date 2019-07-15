n = int(input('Введите число: '))
fib = [0, 1]
index = 2
while fib[len(fib) - 1] <= n:
    fib.append(fib[index - 1] + fib[index - 2])
    index += 1
if fib[len(fib) - 1] >= n:
    del fib[len(fib) - 1]
print(fib)
