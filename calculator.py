number1 = float(input("Enter first number: "))
operation = input("Select an operation (+, -, *, /): ")
number2 = float(input("Enter second number: "))

if operation == "+":
    result = number1 + number2
    print("Result: ", result)
elif operation == "-":
    result = number1 - number2
    print("Result: ", result)
elif operation == "*":
    result = number1 * number2
    print("Result: ", result)
elif operation == "/":
    if number2 == 0:
        print("Error: division by zero is not allowed!")
    else:
        result = number1 / number2
        print("Result: ", result)
