def rob(nums: list[int]) -> int:

    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2,n):

        dp[i] = max((nums[i] + dp[i-2]), dp[i-1]) # max(rob,skip)

    return dp[n-1]

nums = [2,1,1,13]
print(rob(nums))