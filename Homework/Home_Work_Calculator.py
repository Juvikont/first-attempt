print('Welcome to Calculator')
x = float(input("Please provide the first number:"))
z = input("Please choose the operation: (+), (-), (*), (/)")
y = float(input("Please provide the second number:"))
value = 0
while True:
    if z == "+":
        value += x + y
    elif z == "-":
        value += x - y

    elif z == "*":
        value += x * y
    elif z == "/":
        value += x / y

    else:
        print("Wrong operation!")
    a = input('Хотите ввести еще числа?y/n ')
    if a == str('y'):
        x = float(input("Please provide the first number:"))
        z = input('Please choose the operation: (+), (-), (*), (/)')
        y = float(input("Please provide the second number:"))
    else:
        break
print(value)
