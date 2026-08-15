# this is norm fibonnachi siries
def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(7))


# for Dynamic Programming Dp for top down approch

def fib_dp(n,dp):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    elif dp[n] != -1:
        return dp[n]
    
    else:
        return fib_dp(n-1,dp) + fib_dp(n-2,dp)
n = 7  
dp = [-1] * (n+1)  # size of list
print(fib_dp(n,dp))


# for Dynamic Programming Dp for bottom up approch also called tabing
def fib_dp_bu(n,dp):
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] 

n = 7 
dp = [0] * (n+1)
print(fib_dp_bu(n,dp))

# Bonus: Space Optimization
def fib_space(n):
    if n <= 1:
        return n
    
    prev1,prev2 = 0,1

    for _ in range(2,n+1):
        prev1,prev2 = prev2, prev1+prev2

    return prev2

print(fib_space(7))