
# Q1: division with exception handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a/b)
    print("Program executed successfully")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except:
    print("Error: Invalid input")
