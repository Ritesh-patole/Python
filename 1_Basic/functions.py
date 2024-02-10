# Regular Function
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

# Function with Default Parameters
def power(base, exponent=2):
    """This function calculates the power of a number."""
    result = base ** exponent
    return result

# Function with Return Statement
def multiply(a, b):
    """This function multiplies two numbers and returns the result."""
    return a * b

# Function with Docstring
def square(number):
    """
    This function calculates the square of a number.
    
    Parameters:
    number (int): The input number.
    
    Returns:
    int: The square of the input number.
    """
    return number ** 2

# Function with Global and Local Variables
global_variable = 10

def function_with_local_variable():
    local_variable = 5
    print("Local Variable:", local_variable)

# Lambda Function
square_lambda = lambda x: x ** 2

# Recursive Function
def factorial(n):
    """This function calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Function Calls
greet("Alice")
power_result1 = power(2)      # Uses default exponent (2)
power_result2 = power(2, 3)   # Uses provided exponent (3)
product = multiply(4, 6)
square_result = square(3)
function_with_local_variable()
lambda_result = square_lambda(3)
factorial_result = factorial(5)

# Displaying Results
print("Power Result 1:", power_result1)
print("Power Result 2:", power_result2)
print("Product:", product)
print("Square Result:", square_result)
print("Lambda Square Result:", lambda_result)
print("Factorial Result:", factorial_result)
print("Global Variable:", global_variable)
