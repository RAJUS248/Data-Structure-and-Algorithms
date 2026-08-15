def maximumLength(nums):

    seen = {}

    for num in nums:
        seen[num] = seen.get(num,0) + 1

    res = []
    for num in nums:

        count = 1
        pow = 2

        x = num
        while seen[x] >= 2:

            if x == 1 and seen[x] > 2:
                seen[x] -= 2
                count += 2
                
            elif x == 1 and seen[x] >= 2:
                break

            
            x = num ** pow

            if x not in seen:
                break

            elif x != 1:
                count += 2
                pow *= 2

        res.append(count)
        
    
    return max(res)

nums = [2,2,4,4]#[1,1,1,1,1,1,1,1,1,1,2,4,8,16,32,64,128,256,512,1024]#[14,14,196,196,38416,38416] #[5,4,1,2,2] # [2,5,1,4,16,4,2]
print(maximumLength(nums))

class Solution(object):
    def maximumLength(self, nums):
        
        seen = {}

        for num in nums:
            seen[num] = seen.get(num,0) + 1

        res = 1
        there = {1}

        if 1 in seen:
            res = max(1,seen[1] - (seen[1] % 2 == 0))

        for num in nums:
            
            if num not in there and seen[num] >= 2:

                there.add(num)
                count = 1
                pow = 2
                
                x = num

                while x in seen:
                    
                    x = num ** pow

                    if x not in seen:
                        break
                    
                    
                    count += 2
                    pow *= 2

                if count > res:
                    res = count
            
        
        return res
            
            