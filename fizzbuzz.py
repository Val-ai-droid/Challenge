def fizzbuzz(n):
    if n % 15 == 0:
        return "ThreeFive"
    elif n % 3 == 0:
        return "Three"
    elif n % 5 == 0:
        return "Five"
    else:
        return str(n)

    for i in range (1,21):
        print(fizzbuzz(i), end=" ")
        