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



def Find_Transition_Point_v2(arr):

    low = 0
    high = len(arr)-1

    t_point = -1

    while low <= high:

        mid = (low + high)//2

        if arr[mid] == 1:
            
            t_point = mid

            high = mid - 1

        else:

            low = mid + 1

    return t_point

arr = [0,0,0,1,1, 1, 1]
print(Find_Transition_Point_v2(arr))



