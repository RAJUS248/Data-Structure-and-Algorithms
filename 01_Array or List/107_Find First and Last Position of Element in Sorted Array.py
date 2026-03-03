def searchRange(nums, target):

    res = [-1,-1]
    i = 0
    j = 0

    while i < len(nums):

        if nums[i] == target:
            res[0] = j
            res[1] = i

        else:
            j += 1

        i += 1

    return res

nums = [1,2,3,4]
target = 3
print(searchRange(nums,target))


def searchRange_v2(nums, target):

    l ,r = 0, len(nums)-1
    first = last = -1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] >= target:
            r = mid - 1

        else:
            l = mid + 1

        if nums[mid] == target:
            first = mid


    l ,r = 0, len(nums)-1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] <= target:
            l = mid + 1

        else:
            r = mid - 1

        if nums[mid] == target:
            last = mid

    return [first,last]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange_v2(nums,target))