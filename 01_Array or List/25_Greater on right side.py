def greater_on_right_side(arr):
    n = len(arr)
    max_right = arr[n-1]

    arr[n-1] = -1

    for i in range(n-2,-1,-1):

        temp = arr[i]

        arr[i] = max_right

        if max_right < temp:
            max_right = temp


    return arr

arr = [16, 17, 4, 3, -1, 2]

print(greater_on_right_side(arr))