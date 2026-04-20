def canBeEqual(target, arr):
    # if sorted(arr) == sorted(target):
    #     return True
    
    # else:
    #     return False

    # if arr!=target:
    #     arr.sort()
    #     target.sort()
    #     if target==arr:
    #         return True
    #     else: 
    #         return False
    # else:
    #     return True

    if arr == target:
        return True
    
    for num in arr:
        if num not in target:
            return False
        
        target.remove(num)

    return True

target = [3,11,7,9,9]
arr = [3,7,9,11,8]
print(canBeEqual(target,arr))