def subarraysDivByK(nums, k):

    seen = {0:1}

    res = 0
    prefix_sum = 0

    for num in nums:

        prefix_sum += num
        rem = prefix_sum % k

        if rem < 0:
            rem = k + rem

        if rem not in seen:
            seen[rem] = 1

        else:
            res += seen[rem]
            seen[rem] += 1

    return res

nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums,k))