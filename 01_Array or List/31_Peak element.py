def Peak_element(arr):

    n = len(arr)

    if n == 1:
        return 0

    if arr[0] > arr[1]:
        return 0
    
    if arr[n-1] > arr[n-2]:
        return n-1
    
    for i in range(1,n-1):

        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:

            return i
        
    return -1



arr = [1,6,4,5,7,8,3]

print(Peak_element(arr))


# or

def Peak_element_v2(arr):

    n = len(arr)

    if n == 1:
        return 0

    if arr[0] > arr[1]:
        return 0
    
    if arr[n-1] > arr[n-2]:
        return n-1
    
    low = 1
    high = n-2

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        
        elif arr[mid] < arr[mid+1]:
            low = mid + 1

        else: # (this means arr[mid] < arr[mid-1])
            high = mid - 1

    return -1


arr = [1,6,4,5,7,8,3]

print(Peak_element_v2(arr))

