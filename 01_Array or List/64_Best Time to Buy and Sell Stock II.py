def getMaximumProfit(values, n):

    profit = 0

    for i in range(1,n):
        if values[i-1] < values[i]:

            profit += (values[i] - values[i-1])

        # else:
        #     continue

    return profit


n = 5
values = [1, 5, 3, 8, 12]
print(getMaximumProfit(values,n))