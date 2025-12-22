# o(logn) solution

def search(nums: list, target: int):

    # write your code logic !!

    left = 0
    right = len(nums)-1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:

            return mid
        
        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1

    
nums = [1, 2, 3, 4, 5, 6, 7]
target = 7

print(search(nums,target))




# this is o(n) solution

def search_v2(nums: list, target: int):

    # write your code logic !!

    seen = {}

    for idx,val in enumerate(nums):

        seen[val] = seen.get(val,0) + idx

    
    if target in seen:

        return seen[target]
    
    else:
        return -1
    
nums = [1, 2, 3, 4, 5, 6, 7]
target = 3

print(search_v2(nums,target))