def removeDuplicates(nums):

    write = 0

    for read in range(len(nums)):

        if write < 2 or nums[write-2] != nums[read]:
            nums[write] = nums[read]
            write += 1


    return write
           

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))