def compareTriplets(a : int, b: int):
    # Write your code here
    for i in range (a,b):
        if a[i] > b[i]:
            return a[i]
        elif a[i] == b [i]:
            return 0
        elif a[i] < b[i]:
            return b[i]
        else:
            return False
    
a = 5,6,7 
b = 3,6,10 

print("a,b", compareTriplets(a,b))

