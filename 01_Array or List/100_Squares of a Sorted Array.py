
def sortedSquares(nums):
    
    i = 0
    j = pos = len(nums)-1
    
    sqr_list = [0] * len(nums)

    while i <= j:

        l_sqr = nums[i] * nums[i]
        h_sqr = nums[j] * nums[j]

        if  l_sqr < h_sqr:
            sqr_list[pos] = h_sqr
            j -= 1

        else:
            sqr_list[pos] = l_sqr
            i += 1

        pos -= 1    

    return sqr_list 


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
        