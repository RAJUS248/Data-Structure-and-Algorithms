def findLHS(nums):

       
    seen = {}

    for num in nums: 
        seen[num] = seen.get(num,0)+1

    maxi = 0
    for i in range(1,len(nums)):

        if i+1 and i in seen:
            maxi = max(maxi,(seen[i] + seen[i+1]))

    return maxi

nums = [1,3,2,2,5,2,3,7]
# print(findLHS(nums))
def

    
