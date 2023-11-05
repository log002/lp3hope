class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack(items, cap):
    items.sort(key = lambda x:x.ratio, reverse = True)
    
    wt = 0
    p = 0
    for i in range(len(items)):
        if(cap == 0):
            break
        if items[i].weight <= cap:
            p += items[i].value
            cap -= items[i].weight
        elif items[i].weight > cap:
            p += cap * items[i].ratio
            cap = 0
    return p
    
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    cap = int(input("Enter the capacity of knapsack: "))
    items = []
    
    for i in range(0, n):
        w = int(input("enter the weight"))
        val = int(input("enter the value"))
        
        items.append(Item(val, w))
        
    print("The max profit will be ", knapsack(items, cap))
