def missingInteger(nums: list[int]) -> int:
        
    sq_sum = sum(nums[:3])

    seen = set(nums)

    if sq_sum not in seen:
        return sq_sum

    else:

        while sq_sum in seen:

            sq_sum += 1

        return sq_sum
    
nums = [1,2,3,2,5]
print(missingInteger(nums))