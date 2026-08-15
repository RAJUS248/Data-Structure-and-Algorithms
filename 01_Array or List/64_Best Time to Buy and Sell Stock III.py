def maxstock(prices):

    n = len(prices)

    left_profits = [0] * n
    min_price = prices[0]

    for i in range(1,n):  # [3,3,5,0,0,3,1,4]

        profit_today = prices[i] - min_price

        left_profits[i] = max(left_profits[i-1],profit_today)

        min_price = min(min_price,prices[i])

    
    
    right_profits = [0] * n
    max_price = prices[-1]

    for i in range(n-2,-1,-1): # [3,3,5,0,0,3,1,4]

        profit_today = max_price - prices[i]

        right_profits[i] = max(right_profits[i+1],profit_today)

        max_price = max(max_price,prices[i])

    max_prof = 0

    for i in range(n):

        max_prof = max(max_prof,(right_profits[i] + left_profits[i]))

    return left_profits,right_profits,max_prof

prices = [3,3,5,0,0,3,1,4]
print(maxstock(prices))