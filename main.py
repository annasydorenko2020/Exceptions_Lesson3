Task1

try:
    number = int(input("Enter day number: "))

    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
    else:
        print("Invalid number")
except Exception as error:
    print(f"Exception occured: {error}")

Task2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 == num2:
        print("True")
    else:
        print("False")
    if num1 > num2:
        print(num2, num1)
    elif num1 < num2:
        print(num1, num2)
except ValueError as error:
    print("Enter only integer numbers!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occured: {error}")


Task3

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    action = input("Action: ")

    if action == "+":
        print("Sum: ", num1+num2)
    elif action == "-":
        print("Substraction: ", num1-num2)
    elif action == "*":
        print("Multiplication: ", num1*num2)
    elif action == "/":
        print("Division: ", num1/num2)
except ZeroDivisionError as error:
    print(f"ZeroDivision Error occured: {error}")
except ValueError as error:
    print(f"Enter only integer numbers, please: {error}")
except Exception as error:
    print(f"Exception occured: {error}")

