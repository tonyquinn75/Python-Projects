try:
    value = 10/0
    number = int(input("Enter a number"))
print(number)
except ZeroDivisionError as err:
print("Divide by zero")
except ValueError
print("Invalid number")
