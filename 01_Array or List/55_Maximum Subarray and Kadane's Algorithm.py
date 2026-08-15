def maxSubarraySum(arr):

    maxi = float('-inf')
    cur_sum = 0

    for num in arr:

        cur_sum += num

        if cur_sum > maxi:
            maxi = cur_sum

        if cur_sum < 0:
            cur_sum = 0

    return maxi


arr = [-3,-2,-6,-1,-7,-4]
print(maxSubarraySum(arr))