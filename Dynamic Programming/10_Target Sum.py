def findTargetSumWays(nums: list[int], target: int) -> int:
        
    # posible num - not posible num = target
    # P - N = target

    # P + N = total

    # (P + N) + (P - N) = total + target
    # 2P = total + target
    # P = (total + target) // 2

    total = sum(nums)

    if total + target < 0:
        return 0

    if (total + target) % 2 != 0:
        return 0

    p = (total + target) // 2

    dp = [0] * (p + 1)

    dp[0] = 1

    for num in nums:

        for i in range(p,num-1,-1):

            dp[i] += dp[i- num]

    return dp[p]

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums,target))
                

        