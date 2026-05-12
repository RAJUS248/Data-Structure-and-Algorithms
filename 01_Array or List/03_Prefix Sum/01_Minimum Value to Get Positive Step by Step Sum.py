def minStartValue(nums):

    min_pref_sum = float('inf')
    pref_sum = 0

    for num in nums:

        pref_sum += num

        min_pref_sum = min(min_pref_sum,pref_sum)

    StartValue = 1 - min_pref_sum

    if StartValue <= 0:
        return 1
    
    return StartValue
    
nums = [2,3,5,-5,-1] #[-3,2,-3,4,2]
print(minStartValue(nums))

