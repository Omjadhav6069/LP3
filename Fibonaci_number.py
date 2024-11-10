def fibonacci_recursive(n, prev=0, curr=1, i=0, sequence=None):
    if sequence is None:
        sequence = []  # Initialize the list to store Fibonacci sequence

    # Base case: If the current position reaches n, return the sequence
    if i >= n:
        return sequence
    
    # Add the current Fibonacci number to the sequence
    sequence.append(prev)
    
    # Recursive call for the next Fibonacci number
    return fibonacci_recursive(n, curr, prev + curr, i + 1, sequence)

def fibonacci_iterative(n):
    sequence = []
    prev, curr = 0, 1

    for _ in range(n):
        sequence.append(prev)
        prev, curr = curr, prev + curr

    return sequence

# User-driven selection for the Fibonacci sequence generation method
method = input("Choose the method (recursive/iterative): ").strip().lower()
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate and print the Fibonacci sequence based on the chosen method
if method == 'recursive':
    print("Fibonacci sequence (recursive):", fibonacci_recursive(n))
elif method == 'iterative':
    print("Fibonacci sequence (iterative):", fibonacci_iterative(n))
else:
    print("Invalid method. Please choose 'recursive' or 'iterative'.")