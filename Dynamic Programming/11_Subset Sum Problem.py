def isSubsetSum(arr: list[int], sum: int) -> bool:
    
    dp = [False] * (sum+1)
    
    dp[0] = True
    
    for num in arr:             
        
        for s in range(sum,num-1,-1):
            
            if dp[s-num]:    
                dp[s] = True
                
    
    return dp[sum]

arr = [2, 3, 7]
sum = 7
print(isSubsetSum(arr,sum))
