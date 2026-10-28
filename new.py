x = input("Введи число: ")
x = int(x)
if x % 2 == 0:
    print("Парне")
else:
    print("Непарне")


a, b, c = 4, 9, 2
if a >= b and a >= c:
    print(a)
elif b >= a and b >=c:
    print(b)
else:
    print(c)

a = float(input("First number:"))
b = float(input("Second number:"))
op = input("operation (+-*/):")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    
    if b == 0:
        print("You cannot divide by zero")
    else:
        print(a/b)
else:
    print("unknown operation")

    year = int(input( "Year:"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("leap")
    else:
        print("non-leap")



