def minCostClimbingStairs(cost):
        
    n = len(cost)

    mincost = [0] * (n+1)

    for i in range(2,n+1):

        mincost[i] = min(cost[i-1] + mincost[i-1],cost[i-2] + mincost[i-2])

    return mincost[n]

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))