while True:
    number1 = float(input("Enter first number: "))
    operation = input("Select an operation (+, -, *, /): ")
    number2 = float(input("Enter second number: "))

    match operation:
        case "+":
            result = number1 + number2
            print("Result: ", result)
        case "-":
            result = number1 - number2
            print("Result: ", result)
        case "*":
            result = number1 * number2
            print("Result: ", result)
        case "/":
            if number2 == 0:
                print("Error: division by zero is not allowed!")
            else:
                result = number1 / number2
                print("Result: ", result)

    continue_calculating = input("Do you want to continue? (y/n): ")
    if continue_calculating != 'y':
        break