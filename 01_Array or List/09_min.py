def min_arr(arr):
    mini = float("inf")

    for num in arr:
        if num < mini:
            mini = num

    print(mini)

arr = [2,5,-1,-2,3,7,9,10,6]
min_arr(arr)