class Calculator:
    def __init__(self):
        self.history = []
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
calc = Calculator()

while True:
    choice = input("Enter operation, 1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide, 5 - History, 6 - Exit: ")
    if choice == "1":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calc.add(a, b)
            print(a, "+", b, "=", result)
            calc.history.append(f"{a} + {b} = {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif choice == "2":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calc.subtract(a, b)
            print(a, "-", b, "=", result)
            calc.history.append(f"{a} - {b} = {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif choice == "3":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calc.multiply(a, b)
            print(a, "*", b, "=", result)
            calc.history.append(f"{a} * {b} = {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif choice == "4":
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calc.divide(a, b)
            print(a, "/", b, "=", result)
            calc.history.append(f"{a} / {b} = {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    elif choice == "5":
        print("Calculation History:")
        for entry in calc.history:
            print(entry)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")