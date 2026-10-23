
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
    