print('Welcome to Calculator')
x = float(input("Please provide the first number:"))
y = float(input("Please provide the second number:"))
z = input("Please choose the operation: (+), (-), (*), (/)")
if z == "+":
    z = x + y
    print ("=" + str(z))
elif z == "-":
    z = x - y
    print ("="+str(z))
elif z == "*":
    z = x*y
    print ("=" + str(z))
elif z == "/":
    z = x/y
    print ("=" + str(z))
else:
    print ("Wrong operation!")