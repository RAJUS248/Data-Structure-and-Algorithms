def knapsack(W,val,wt):
    
    dp = [0] * (W + 1)

    for i in range(len(val)):

        for j in range(W,wt[i]-1,-1):

            dp[j] = max(dp[j], val[i] + dp[j - wt[i]])

    return dp[W]
        
    
W = 5 
val = [10, 40, 30, 50]
wt = [5, 4, 2, 3] 
print(knapsack(W,val,wt))


def knapsack_v2(W,val,wt):
    
    def func(i,w):

        if i == 0:
            if wt[i] <= w:
                return val[i]
            
            return 0
        if wt[i] > w:
            pick = float('-inf')

        else:
            pick = val[i] + func(i-1,w-wt[i])

        not_pick = 0 + func(i-1,w)

        return max(pick,not_pick)

    print(func(len(val)-1,W))
        
    
W = 5 
val = [10, 40, 30, 50]
wt = [5, 4, 2, 3] 
knapsack_v2(W,val,wt)
