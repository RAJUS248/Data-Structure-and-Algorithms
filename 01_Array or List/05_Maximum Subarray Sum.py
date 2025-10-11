def max_subarr(arr):
    max_sum = float("-inf")
    cur_sum = 0

    for num in arr:
        cur_sum += num

        max_sum = max(max_sum,cur_sum)

        if cur_sum < 0:
            cur_sum = 0 

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarr(arr)) 