def findDuplicates(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num,0)+1

    res = []

    for key,val in count.items():
        if val >= 2:
            res.append(key)

    return res

def findDuplicates_v2(nums):

    seen = set()

    dublicate = []
    for num in nums:
        if num not in seen:
            seen.add(num)
        
        else:
            dublicate.append(num)

    return dublicate

def findDublicates_v3(nums):

    res = []
    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            res.append(abs(num))

        else:
            nums[index] = - nums[index]

    return res

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
print(findDuplicates_v2(nums))
print(findDublicates_v3(nums))