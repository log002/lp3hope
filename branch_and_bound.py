class Item:
    def __init__(self,value,weight):
        self.weight=weight
        self.value=value
        self.ratio=value/weight
        
    
def knapsack(items,capacity):
        items.sort(key=lambda x:x.ratio,reverse=True)
        
        def bound(i,current_weight,current_value):
            
            if(current_weight>=capacity):
                return 0
            j=i
            bound_value=current_value
            
            while j<len(items) and current_weight+items[j].weight<capacity:
                current_weight+=items[j].weight
                bound_value+=items[j].value
                j+=1
                
            
            if(j<len(items)):
                bound_value+=(capacity-current_weight)*items[j].ratio
                
            return bound_value
        
        def branch_and_bound(i,current_weight,current_value):
            nonlocal maxvalue
            
            if(current_weight<=capacity and current_value>maxvalue):
                maxvalue=current_value
                
            if(i==len(items)):
                return
            
            if(current_weight+items[i].weight<=capacity):
                branch_and_bound(i+1,current_weight+items[i].weight,current_value+items[i].value)
                
            
            if(bound(i+1,current_weight,current_value)>maxvalue):
                branch_and_bound(i+1,current_weight,current_value)
                
        maxvalue=0
        branch_and_bound(0,0,0)
        return maxvalue
            
            
capacity=int(input(" Enter the capacity of knapsack "))
n=int(input("enter the number of items "))

items=[]
for i in range (0,n):
    weight=int(input("Enter the weight "))
    value=int(input("Enter the value "))
    items.append(Item(value,weight))
    

max_value=knapsack(items,capacity)
print("max_value = ",max_value)
