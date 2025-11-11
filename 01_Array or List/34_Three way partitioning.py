def three_way(arr,a,b):

    low = 0
    mid = 0
    high = len(arr)-1


    while mid <= high:

        if arr[mid] < a:
            arr[low],arr[mid] = arr[mid],arr[low]

            low += 1
            mid += 1
            
        elif arr[mid] > b:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

        else:
            mid += 1

    return arr

arr = [1, 4, 3, 6, 2, 1]
a = 1
b = 3

print(three_way(arr,a,b))