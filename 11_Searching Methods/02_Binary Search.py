def binary_search(arr,key):
    l = 0
    r = len(arr) - 1

    while l <= r:

        mid = (r + l)//2

        if  arr[mid] == key:
            return 'key found'
        
        elif key < arr[mid]:
            r = mid - 1

        else:
            l = mid + 1

    return 'Key not found'

arr = [1,2,3,5,6,8,9]
key = 5
result = binary_search(arr,key)
print(result)