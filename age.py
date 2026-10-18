age = 25
height = 170

if age >= 20 and age <= 30 and height >= 170:
    
    print("Вік знаходиться в межах від 20 до 30 років.")
elif age < 20 or age > 40 and height < 170:
    print("Вік  знаходиться в межах від 31 до 40 років.")
else:
 print("Вік не входить в межі від 20 до 40 років або зріст менше 170 см.")

# i = 1
# while i < 20:
# i += 1
# if i % 2 == 0:
#     print("Парне число:", i)
else:
print(f"Непарне число: {i}")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print("Found a banana!")
    else:
        print("Not a banana:", fruit)
