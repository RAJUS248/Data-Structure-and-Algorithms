def MinimumOperations(arr):

    seen = {0}
    cur_sum = 0
    ops = 0

    for num in arr:
        cur_sum += num
        if cur_sum in seen:
            ops += 1
            seen = {0}   
            cur_sum = num

        seen.add(cur_sum)

    return ops

arr = [10,20,-10]
print(MinimumOperations(arr))