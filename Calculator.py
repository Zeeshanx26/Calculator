def calculator ():

    print("Welcome to Calculator")
    print("Select Operations +, -, *, / ")
    try:

        operator = input("Enter Operator: ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("The sum is: ", num1 + num2)
        elif operator == "-":
            print("The difference is: ", num1 - num2)
        elif operator == "*":
            print("The multiplication is: ", num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Error.")
                return
            print("The Division is: ", num1 / num2)

        else:
            print("Invalid operator")
            return



    except ValueError:
        print("Invalid input")
        return


if __name__ == "__main__":
    calculator()