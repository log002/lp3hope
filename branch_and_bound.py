class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def knapsack(items, cap):
    items.sort(key = lambda x:x.ratio, reverse = True)
    def bound(i, curr_wt, curr_val):
        if(curr_wt >= cap):
            return 0
        j = i
        bound_val = curr_val
        while j < len(items) and curr_wt + items[j].weight < cap:
            curr_wt += items[j].weight
            bound_val += items[j].value
            j += 1
        if j < len(items):
            bound_val += (cap - curr_wt) * items[j].ratio
        return bound_val
    
    def branch_and_bound(i, curr_wt, curr_val):
        nonlocal maxval
        if(curr_wt <= cap and curr_val > maxval):
            maxval = curr_val
        
        if i == len(items):
            return
    
        if(curr_wt + items[i].weight <= cap):
            branch_and_bound(i + 1, curr_wt + items[i].weight, curr_val + items[i].value)
        
        if(bound(i + 1, curr_wt, curr_val) > maxval):
            branch_and_bound(i + 1, curr_wt, curr_val)
    maxval = 0
    branch_and_bound(0,0,0)
    return maxval

cap = int(input("Enter the capacity of knapsack: "))
n = int(input("Enter the number of items: "))

items = []
for i in range(n):
    wt = int(input("Enter the weight "))
    val = int(input("enter the value" ))
    items.append(Item(val,wt))
    
max_val = knapsack(items, cap)
print("Max profit is ", max_val)
