def Contains_Duplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return True
        
        seen.add(num)

    return False

arr = [1,2,3,4]
print(Contains_Duplicate(arr))