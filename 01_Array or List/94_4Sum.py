def fourSum(nums, target):

    nums.sort()
    n = len(nums)

    res = []
    for i in range(n-3):

        if i > 0 and nums[i] == nums[i - 1]:
                continue
        
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            break

        if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
        
        for j in range(i+1,n-2):

            left = j + 1
            right = n - 1

            if j > i + 1 and nums[j] == nums[j-1]:
                continue

            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                break
            
            if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                continue
            
            
            while left < right:

                the_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if the_sum == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif the_sum < target:
                    left += 1
                
                else:
                    right -= 1

    return res



nums = [-3,-2,-1,0,0,1,2,3] # [1,0,-1,0,-2,2]
target = 0
# nums = [2,2,2,2,2]
# target = 8
print(fourSum(nums,target))