def knapSack(val, wt, capacity):
        
    n = len(val)
    
    dp =[[0] * (capacity+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        
        for j in range(1,capacity+1):
            
            if wt[i-1] <= j:
                
                inc = val[i-1] + dp[i][j-wt[i-1]]
                exc = dp[i-1][j]
                
                dp[i][j] = max(inc,exc)
                
            
            else:
                
                dp[i][j] = dp[i-1][j]
                
    return dp[n][capacity]

val = [1, 1]
wt = [2, 1]
capacity = 3

print(knapSack(val,wt,capacity))