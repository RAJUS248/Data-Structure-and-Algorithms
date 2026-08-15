def selection_sort(arr):

    n = len(arr)

    if n <= 1:
        return arr
    
    res = []
    for i in range(n):
        min_idx = i

        for j in range(i+1,n):

            if arr[min_idx] > arr[j]:
                min_idx = j

        res.append(arr[min_idx])

    return res

arr = [4,1,3,7,9]
print(selection_sort(arr))

