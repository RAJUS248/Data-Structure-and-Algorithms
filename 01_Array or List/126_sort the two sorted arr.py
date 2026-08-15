def sort_arr(arr1,arr2):

    i = 0
    j = 0
    res = []
    
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:

            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1

    
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res

    
arr1 = [1,2,4]
arr2 = [1,3,4,5,6,7]
# arr1 = [1, 5, 6]
# arr2 = [2, 3, 4]

print(sort_arr(arr1,arr2))