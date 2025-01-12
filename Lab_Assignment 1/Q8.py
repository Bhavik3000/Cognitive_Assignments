# 8.1 Handle division by zero:
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero. Enter valid input")

# 8.2 Handle invalid input:
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")

# 8.3 Use finally:
try:
    print(10 / 2)
finally:
    print("This will always execute.")
