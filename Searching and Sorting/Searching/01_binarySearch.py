def binarySearch( theValues, target ):

    low = 0
    high = len(theValues)

    while low <= high:

        mid = (low + high) // 2    # (0 + 11) // 2 = 5 -> mid

        if theValues[mid] == target:
            return True
        
        elif theValues[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return False
            

theValues = [2,4,5,10,13,18,23,29,31,51,64]
target = 1
print(binarySearch(theValues,target))