# O(N)
def searchInsert(nums, target):

    for i in range(len(nums)):

        if nums[i] > target:
            return i
        
        if target == nums[i]:
            return i
        
    return i + 1

nums = [1,3,5,6]
target = 7
print(searchInsert(nums,target))

# O(log n)
def searchInsert_v2(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return left


nums = [1,3,5,6]
target = 2
print(searchInsert_v2(nums,target))
