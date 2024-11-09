class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Total value of the knapsack
    for item in items:
        if capacity == 0:
            break
        # Take as much as possible from the current item
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            # Take fraction of the item that fits in the remaining capacity
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is now full

    return total_value

def get_user_input():
    n = int(input("Enter the number of items: "))
    items = []
    
    for i in range(n):
        value = float(input(f"Enter value for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(value, weight))
    
    capacity = float(input("Enter the capacity of the knapsack: "))
    return items, capacity

# Main program
if __name__ == "__main__":
    items, capacity = get_user_input()
    max_value = fractional_knapsack(items, capacity)
    print("Maximum value in the knapsack =", max_value)
