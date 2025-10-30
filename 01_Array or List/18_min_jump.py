def jumping(arr):
    if len(arr) <= 1:
        return 0

    if arr[0] == 0:
        return 0
    
    jump = 0
    max_reach = 0
    cur_end = 0

    for i in range(len(arr)-1):
        max_reach = max(max_reach, i + arr[i])
        if i == cur_end:
            jump += 1
            cur_end = max_reach

        if cur_end >= len(arr)-1:
            return jump

        if i >= max_reach:
            return -1
        
    return -1

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(jumping(arr))

