def Alternate_Positive_Negative(arr):

    pos_arr = []
    neg_arr = []

    for num in arr:

        if num >= 0:
            pos_arr.append(num)

        else:
            neg_arr.append(num)

    arr2 = []

    j = 0

    while j < len(pos_arr) or j < len(neg_arr):

        if j < len(pos_arr):

            arr2.append(pos_arr[j])

        if j < len(neg_arr):

            arr2.append(neg_arr[j])

        j += 1
    
    for k in range(len(arr)):

        arr[k] = arr2[k]

    return arr

arr = [9,4,-2,-1,5,0,-5,-3,2]

print(Alternate_Positive_Negative(arr))
