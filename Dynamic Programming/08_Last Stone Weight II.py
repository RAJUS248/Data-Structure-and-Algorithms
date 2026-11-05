def lastStoneWeightII(stones: list[int]) -> int:
        
    total = sum(stones)

    target = total // 2

    n = len(stones)

    dp = [[0] * (target + 1) for _ in range(n+1)]

    for i in range(1,n+1):

        for j in range(1,target + 1):

            if stones[i-1] <= j:

                inc = stones[i-1] + dp[i-1][j - stones[i-1]]
                exc = dp[i-1][j]

                dp[i][j] = max(inc,exc)

            else:
                dp[i][j] = dp[i-1][j]

    best = dp[n][target]

    return total - (2 * best)

stones = [2,7,4,1,8,1]
print(lastStoneWeightII(stones))