def stock_buy_sell(arr):
    
    min_buy = float('inf')
    max_prof = 0

    for num in arr:

        if min_buy > num:
            min_buy = num
        
        else:
            
            max_prof = max(max_prof,(num - min_buy))

    return max_prof

arr = [5,4,1,3,2,9,2,4]
print(stock_buy_sell(arr))