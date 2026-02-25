def sortColors(nums):
    l = 0
    m = 0
    h = len(nums)-1

    while m <= h :

        if nums[m] == 0:
            nums[l],nums[m] = nums[m],nums[l]
            l += 1
            m += 1
        
        elif nums[m] == 2:
            nums[h],nums[m] = nums[m],nums[h]
            h -= 1

        else:
            m += 1

    return nums

nums = [2,0,2,1,1,0] # [2,0,1]
print(sortColors(nums))