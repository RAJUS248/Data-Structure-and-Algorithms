def insertion_sort(arr):
    size = len(arr)

    for i in range(1,size):
        key = arr[i]
        
        for j in range(i-1,-1,-1):

            if key < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = key

            else:
                break

    return arr

arr = [1,2,3,4, 5, 4, 3, 2]
print(insertion_sort(arr))