
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
        print(number)

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

        total = 0
        for number in numbers:
            total += number
        print(f"Total: {total}")

num1 = 10
num2 = 20
    #accept input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

    # calculate multiplication
result = num1 * num2

    # display result
print("The multiplication is:", result)

#using sep parameter to join strings
print("name", "is", "James", sep="***")

num = 8
# using %0 to format the integer as octal
print("%0" % num)

Name1 = Emma
Name2 = Jessa
Name3 = Kelly

# Taking multiple inputs in one go
str1, str2, str3 = input("Enter three names: ").split()

print("Name1:", str1)
print("Name2:", str2)
print("Name3:", str3)

