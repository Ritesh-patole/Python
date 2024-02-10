def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    while True:
        print("\n===== Simple Calculator =====")
        print("Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")

        choice = input("Select operation (1/2/3/4/0): ")

        if choice == '0':
            print("\nExiting the calculator. Goodbye!")
            break  # Exit the while loop

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")

        elif choice == '0':
            print("\nExiting the calculator. Goodbye!")
            break  # Exit the while loop

        else:
            print("\nInvalid Input. Please enter a valid option.")

# Run 
calculator()
