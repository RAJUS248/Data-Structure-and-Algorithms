def containsNearbyDuplicate(nums, k):
        
        seen = set()
        for j in range(len(nums)):

            if nums[j] not in seen:
                seen.add(nums[j])

            else:
                i = 0
                while i < j:

                    if nums[i] == nums[j] and abs(i-j) <= k:
                        return True
                    
                    i += 1
           
        return False
def containsNearbyDuplicate_v2(nums, k):
     
    seen = set()
    
    l = 0
    for r in range(len(nums)):
        if r - l > k:
            seen.remove(nums[l])
            l += 1
        
        if nums[r] in seen:
            return True
        seen.add(nums[r])
    return False

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums,k))
print(containsNearbyDuplicate_v2(nums,k))