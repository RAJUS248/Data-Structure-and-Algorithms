def search_element(nums, target):
    for index in range(len(nums)):
        if nums[index] == target:
            return index

    return -1

nums = [3,7,8,0,-2,7,2,5,6]
target = 7

print(search_element(nums,target))