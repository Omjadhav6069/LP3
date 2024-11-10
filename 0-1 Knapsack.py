def knapsack_01(items,capacity,n):
    
    dp=[[0 for _ in range(capacity+1)] for _ in range (n+1)]
    
    for i in range(1,n+1):
        for w in range(capacity +1):
            if items[i-1].weight<=w:
                dp[i][w]=max(dp[i-1][w],dp[i-1][w-items[i-1].weight]+items[i-1].value)
            else:
                dp[i][w]=dp[i-1][w]
                
    return dp[n][capacity]

class Item:
    def _init_(self,value,weight):
        self.value=value
        self.weight=weight
        
capacity=int(input("Enter the capacity of knapsack : "))
n=int(input("Enter the number of items : "))

items=[]

for i in range(n):
    value=int(input("Enter the value of item "+str(i+1)+" : "))
    weight=int(input("Enter the weight of item "+str(i+1)+" : "))
    
    obj=Item(value,weight)
    items.append(obj)

max_value=knapsack_01(items,capacity,n)

print("Maximum value in the knapsack is : ",max_value)
