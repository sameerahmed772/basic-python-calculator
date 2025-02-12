#My first python calculator program
import math

print("Enter the calculator function you want to use (1-6): ")
func = input("1. + \n2. -\n3. *\n4. /\n5. %\n6. square root\n")

if func == "1":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The result is = {a + b}")
elif func == "2":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The result is = {a - b}")
elif func == "3":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The result is = {a * b}")
elif func == "4":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed!")
    else:
        print(f"The result is = {a / b}")
elif func == "5":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(f"The result is = {a % b}")
elif func == "6":
    a = float(input("Enter any number: "))
    if a < 0:
        print("Math Error: Square root of a negative number is not possible!")
    else:
        print(f"The square root of {a} is = {math.sqrt(a)}")
else:
    print("Please select a valid option between 1-6!")
