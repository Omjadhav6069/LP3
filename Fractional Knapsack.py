class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.value_per_weight = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by their value per weight ratio in descending order
    items.sort(key=lambda item: item.value_per_weight, reverse=True)
    
    total_value = 0.0
    for item in items:
        if capacity - item.weight >= 0:
            # If the item can be added completely
            capacity -= item.weight
            total_value += item.value
        else:
            # If the item cannot be added completely
            total_value += item.value * capacity/ item.weight
            break
            
    return total_value

# Example usage
if __name__ == "__main__":
    #items = [
    #    Item(60, 10),
    #    Item(100, 20),
    #    Item(120, 30),
    #]
    capacity = int(input("Enter the Capacity: "))
    array=[]
    n=int(input("Enter the number of items: "))
    for i in range(0,n):
        value=int(input("Enter the Profit: "))
        weight=int(input("Enter the Weight: "))
        obj=Item(value,weight)
        array.append(obj)
    
    
    max_value = fractional_knapsack(capacity, array)
    print(f"Maximum value in Knapsack = {max_value}")
