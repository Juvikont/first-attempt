def reverse(func):
    def wrapper(*args):
        return func(*args[::-1])

    return wrapper


def decorator(function):
    def wrapper2(*args):
        print(*args)
        res = function(*args)
        print(function.__name__)
        function(*args)

    return wrapper2


@decorator
def summa(a, b):
    return a + b


print(summa(5, 6))
