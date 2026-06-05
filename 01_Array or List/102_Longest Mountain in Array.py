def longestMountain(arr):

    up = 0
    down = 0
    max_len = 0

    for i in range(len(arr)-1):

        if (down > 0 and arr[i] < arr[i+1]) or arr[i] == arr[i+1]:
              
            up = 0
            down = 0

        if arr[i] < arr[i+1]:
            up += 1

        elif arr[i] > arr[i+1]:
            if up > 0:
                down += 1

        if up > 0 and down > 0:
            max_len = max(max_len,up + down + 1)


    return max_len

arr = [2,1,4,7,3,2,5]
print(longestMountain(arr))
