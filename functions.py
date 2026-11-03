def greet(name):
    return "Hello, " + name + "!"

print(greet("Olga"))
print(greet("Denis"))
print(greet("Sofiya"))

def to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(to_fahrenheit(0))
print(to_fahrenheit(100))

def average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(average([2,4,6,8]))
print(average([]))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n): 
        if n % i == 0:
            return False
    return True

for i in range(2, 31):
    if is_prime(i):
        print(i, end=" ")

def is_strong(password): 
    if len(password) < 8:
        return False
    has_upper = False
    has_digit = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.isdigit():
            has_digit = True 
    return has_upper and has_digit

print(is_strong("abc"))
print(is_strong("Password1"))
     

