def fibonacci(n):
    # Handle base cases
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    
    # Calculate Fibonacci for positive n
    n_positive = abs(n)
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n_positive + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    # Adjust for negative Fibonacci if n < 0
    return fib_curr if n > 0 else (-1) ** (n_positive + 1) * fib_curr

# Take user input
try:
    n = int(input("Enter an integer to calculate its Fibonacci number: "))
    print(f"The Fibonacci number for {n} is: {fibonacci(n)}")
except ValueError:
    print("Invalid input. Please enter an integer.")
