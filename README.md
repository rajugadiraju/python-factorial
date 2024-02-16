# python-factorial
A Sample Python code that calculates factorial of a given number.

def factorial(n):
    """
    Calculates the factorial of a positive integer n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from the user
try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Please enter a positive integer.")
    else:
        print(f"The factorial of {num} is {factorial(num)}.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")

