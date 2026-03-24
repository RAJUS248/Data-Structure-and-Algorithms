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

arr = [1534, 246, 933, 127, 277, 321, 454, 565, 220]
key = 220
result = binary_search(arr,key)
print(result)