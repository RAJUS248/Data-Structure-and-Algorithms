def decompressRLElist(nums):

    res = []

    # for i in range(len(nums)//2):

    #     freq = nums[2*i]
    #     val = nums[2*i+1]

    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i+1]
        res.extend([val] * freq)
        # for _ in range(freq):
        #     res.append(val)

    return res
    
    


nums = [1,2,3,4,5,6]
print(decompressRLElist(nums))