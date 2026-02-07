def threeSumClosest_v2(nums, target):

    nums.sort()
    n = len(nums)


    closest_sum = nums[0] + nums[1] + nums[2]
    
    for i in range(n-2):
        left = i + 1
        right = n-1

        while left < right:

            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == target:
                return cur_sum
            

            if abs(target - cur_sum) < abs(target - closest_sum):
                closest_sum = cur_sum

                
            if cur_sum < target:
                left += 1

            else:
                right -= 1
                
    return closest_sum


nums = [-1,2,1,-4]
# nums = [0,0,0,0]
# nums = [1,-1,1,-1]
# nums = [10,20,30,40,50,60,70,80,90]
target = 1
print(threeSumClosest_v2(nums,target))




# def threeSumClosest(nums, target):

#     nums.sort()
#     n = len(nums)


#     closest_sum = nums[0] + nums[1] + nums[2]
#     best_sum = float('inf')
#     for i in range(n-2):
#         left = i + 1
#         right = n-1

#         while left < right:

#             the_sum = nums[i] + nums[left] + nums[right]

#             if the_sum == target:
#                 return the_sum
            
#             diff = abs(target - the_sum)

#             if diff < closest_sum:
#                 closest_sum = diff
#                 best_sum = the_sum

                
#             if the_sum < target:
#                 left += 1

#             else:
#                 right -= 1
                
#     return best_sum


# # nums = [-1,2,1,-4]
# # nums = [0,0,0,0]
# # nums = [1,-1,1,-1]
# nums = [10,20,30,40,50,60,70,80,90]
# target = 1
# print(threeSumClosest(nums,target))