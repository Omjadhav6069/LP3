def fibonacci(n):
    if n <= 1:
        return n
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    return fib_curr

# Take user input
try:
    n = int(input("Enter a non-negative integer to calculate its Fibonacci number: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")