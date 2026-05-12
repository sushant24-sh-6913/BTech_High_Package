while True:
    m = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    n = float(input("Enter second number: "))

    if op == '+':
        print("Result:", m + n)
    elif op == '-':
        print("Result:", m - n)
    elif op == '*':
        print("Result:", m * n)
    elif op == '/':
        if n == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", m / n)
    else:
        print("Error: Invalid operator")

    again = input("Calculate again? (y/n): ")
    if again.lower() != 'y':
        break

print("Goodbye!")