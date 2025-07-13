try:
    result = 10/1
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("zero error")
except ValueError:
    print("Invalid input")

try:
    result = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as dnd:
    print(dnd)