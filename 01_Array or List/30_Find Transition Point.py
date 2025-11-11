def Find_Transition_Point(arr):

    if arr[0] == 1:
        return -1
    

    for i in range(len(arr)):

        if arr[i] == 0:
            continue

        elif arr[i] == 1:
            return i

    return  -1 

arr = [1, 1, 1]
print(Find_Transition_Point(arr))
