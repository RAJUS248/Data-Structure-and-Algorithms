def selection_sort(arr):

    n = len(arr)
    

    for i in range(n):

        min_idx = i
        for j in range(i+1,n):

            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    return arr

arr = [200,5,9,3,2,8,1,7,0,6,6,4,100]
print(selection_sort(arr))
