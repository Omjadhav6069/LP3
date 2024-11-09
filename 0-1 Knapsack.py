def knapsack_0_1(values, weights, capacity):
    n = len(values)
    
    # Create a DP table to store the maximum value at each capacity and item index
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # The value at dp[n][capacity] will be the maximum value that can be attained
    return dp[n][capacity]

def get_user_input():
    n = int(input("Enter the number of items: "))
    values = []
    weights = []
    
    for i in range(n):
        value = int(input(f"Enter value for item {i+1}: "))
        weight = int(input(f"Enter weight for item {i+1}: "))
        values.append(value)
        weights.append(weight)
    
    capacity = int(input("Enter the capacity of the knapsack: "))
    return values, weights, capacity

# Main program
if __name__ == "__main__":
    values, weights, capacity = get_user_input()
    max_value = knapsack_0_1(values, weights, capacity)
    print("Maximum value in the knapsack =", max_value)
