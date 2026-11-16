def count_vowels(text):
    vowels = "аеєиіїоуюя"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

sentence = input("Sentence: ")
print("Vowels:", count_vowels(sentence))


def deposit(balance):
    amount = float(input("Sum: "))
    if amount < 0:
        print ("The sum must be positive")
        return balance

def withdraw(balance): 
    amount = float(input("Sum: "))
    if amount <= 0 or amount > balance:
        print("It is impossible to withdraw this amount")
        return balance
    return balance - amount

balance = 1000
while True:
    print("1  Top up 2 Withdraw 3 Balance 0 Exit")
    choice = input("> ")
    if choice == "1":
        balance = deposit(balance)
    elif choice == "2":
        balance = withdraw(balance)
    elif choice == "3":
        print("Balance:", balance)
    elif choice == "0":
        break
    else:
        print("Unknown command")

def pyramid(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=" ")
        print()

pyramid(4)

                


        

        