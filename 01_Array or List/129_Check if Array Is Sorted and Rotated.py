def check(nums):
    n = len(nums)
    count = 0
    for i in range(n):

        if nums[i] > nums[(i+1) % n]:
            count += 1

    if count > 1:
        return False
    
    else:
        return True

nums = [3,4,5,1,2]
print(check(nums))



def rotate(nums, k):

        slc = len(nums) - k

        res = nums[slc:] + nums[:slc]

        return res

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))