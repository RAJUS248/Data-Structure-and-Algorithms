def missing_ap(arr):

    if len(arr) < 2:
        return None
    
    d1 = arr[1] - arr[0]
    d2 = arr[-1] - arr[-2]

    diff = d1 if abs(d1) < abs(d2) else d2

    for i in range(len(arr)-1):
        if arr[i] + diff != arr[i+1]:
            return arr[i] + diff
        
    return arr[-1] + diff

arr = [41,21,11]

print(missing_ap(arr))
