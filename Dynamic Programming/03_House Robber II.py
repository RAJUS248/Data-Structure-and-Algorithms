def rob(houses):

    if len(houses) == 1:
        return houses[0]

    def rob_linear(houses):
        n = len(houses)

        if n == 1:
            return houses[0]

        dp = [0] * n

        dp[0] = houses[0]
        dp[1] = min(houses[0],houses[1])

        for i in range(2,n):

            dp[i] = max(dp[i-2] + houses[i], dp[i-1])

        return dp[n-1]

    case1 = rob_linear(houses[1:])
    case2 = rob_linear(houses[:-1])

    return max(case1,case2)

houses = [1,2,3,1]
print(rob(houses))
