def Peak_element(arr):
    i,j,k = 0,1,2

    # for 1 element
    if arr[0] > 0:
        return True
    
    


    while k < len(arr):

        if arr[i] < arr[j] > arr[k]:
            return True
        
        i += 1
        j += 1
        k += 1

    return False

arr = [1, 2, 4, 5, 7, 8, 3]
print(Peak_element(arr))
