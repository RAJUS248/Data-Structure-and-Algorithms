def min_climb(nums):

    n = len(nums)

    dp = [0] * (n+1)

    for i in range(2,n+1):

        dp[i] = min(nums[i-1] + dp[i-1], nums[i-2] + dp[i-2])

    return dp[n]

nums = [10,15,20,10,30]
print(min_climb(nums))