for i in range(1,21):
    if i % 2 == 0:
        print(i)

n = 5 
result = 1
for i in range(1, n + 1):
    result *= i
print(result) 

secret = 42
attempts = 0
while True:
    guess = int(input("Your number: "))
    attempts += 1
    if guess < secret:
        print("More")
    elif guess > secret:
        print("Less")
    else:
        print("Guessed it", attempts, "attempts!")
        break

n =1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
    