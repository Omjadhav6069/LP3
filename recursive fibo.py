def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Taking user input
n = int(input("Enter a number to calculate the Fibonacci sequence: "))
print(f"Fibonacci({n}) = {fibonacci(n)}")
