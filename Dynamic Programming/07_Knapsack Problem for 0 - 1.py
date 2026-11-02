def knapsack01(val,wt,w):

    n = len(val)
    dp = [[0] * (w+1) for _ in range(n+1)]

    for i in range(1,n+1):

        for j in range(1,w+1):

            if wt[i-1] <= j:

                inc = val[i-1] + dp[i-1][j - wt[i-1]]
                exc = dp[i-1][j]

                dp[i][j] = max(inc,exc)

            else:

                dp[i][j] = dp[i-1][j]

    return dp[n][w]

w = 10
val = [20,30,50,60,100]
wt = [2,3,4,5,9]

print(knapsack01(val,wt,w))