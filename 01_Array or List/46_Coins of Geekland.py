def geeks_coins(mat,N,K):

    if N == 1 and K == 1:
        return mat[0][0]
    
    row = N + 1
    col = N + 1

    dp = []
    for _ in range(row):
        new_dp = [0] * col
        dp.append(new_dp)

    for i in range(1,row):
        for j in range(1,col):

            dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    max_sum = float("-inf")
    for i in range(K,row):
        for j in range(K,col):


            total = dp[i][j] - dp[i-K][j] - dp[i][j-K] + dp[i-K][j-K]

            max_sum = max(max_sum,total)

    return max_sum

      
N = 5
K = 3
mat = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2], 
    [3, 8, 6, 7, 3], 
    [4, 4, 4, 4, 4], 
    [5, 5, 5, 5, 5],
]

print(geeks_coins(mat,N,K))