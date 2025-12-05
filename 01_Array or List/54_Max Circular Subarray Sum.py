def maxCircularSum(arr):

    maxi = float('-inf')
    mini = float('inf')

    max_sum = 0
    min_sum = 0

    total_sum = 0

    for num in arr:

        total_sum += num

        max_sum += num

        if maxi < max_sum:
            maxi = max_sum

        if max_sum < 0:
            max_sum = 0

        min_sum += num

        if min_sum < mini:
            mini = min_sum

        if min_sum > 0:
            min_sum = 0

    if maxi < 0:
        return maxi
    
    return max(maxi, total_sum - mini), mini



arr =  [4,2,1,2,6]# [8, -8, 9, -9, 10, -11, 12]

print(maxCircularSum(arr))