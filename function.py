# create the greet function
def greet(name):
    print("Hello," + name)
    # call greet
    greet("Emil")

    def my_function(*numbers):
        total = 0
        for number in numbers:
            total += number
            return total
        print(my_function(1,2,3))
        print(my_function(10,20,30,40))
        print(my_function(5))
        
