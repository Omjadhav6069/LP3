# Non-Recursive (Iterative) Fibonacci Function
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive Fibonacci Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Main function to test both methods
if __name__ == "__main__":
    n = int(input("Enter a number to calculate Fibonacci: "))

    # Calculate using Iterative Method
    print("Iterative Method:")
    iterative_result = fibonacci_iterative(n)
    print(f"Fibonacci({n}) = {iterative_result}")

    # Calculate using Recursive Method
    print("\nRecursive Method:")
    recursive_result = fibonacci_recursive(n)
    print(f"Fibonacci({n}) = {recursive_result}")
