def moving_all_negative_num_to_end(arr):

    temp = []

    for num in arr:
        if num >= 0:
            temp.append(num)

    for num in arr:
        if num < 0:
            temp.append(num)

    for i in range(len(arr)):
        arr[i] = temp[i]

    return arr

arr = [1, -1, 3, 2, -7, -5, 11, 6 ]

print(moving_all_negative_num_to_end(arr))

