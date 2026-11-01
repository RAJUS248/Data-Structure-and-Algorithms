def jump(nums):

    n = len(nums)

    if n == 1:
        return 0

    if n == 1:
        return abs(nums[0] - nums[1])

    INF = float("inf")
    dp = [INF] * n

    dp[0] = 0
    dp[1] = abs(nums[0] - nums[1])

    for i in range(2,n):

        dp[i] = min(dp[i-1] + abs(nums[i] - nums[i-1]), dp[i-2] + abs(nums[i] - nums[i-2]))

    return dp[n-1]

nums = [20, 30, 40, 20]
print(jump(nums))