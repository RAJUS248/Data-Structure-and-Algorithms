def subarraySum(arr, target):

    for i in range(len(arr)):
        total = 0
        for j in range(i,len(arr)):

            total += arr[j]
            if total == target:
                return [i+1,j+1]
            
            if total > target:
                break
            
    return [-1]

arr = [5, 3, 4]
target = 8

print(subarraySum(arr,target))


def subarraySum_v2(arr, target):

    left = 0
    cur_sum = 0

    for right in range(len(arr)):

        cur_sum += arr[right]

        while cur_sum > target and left <= right:

            cur_sum -= arr[left]
            left += 1

        if cur_sum == target and left <= right:

            return [left+1,right+1]
        
    return [-1]

arr = [1, 2, 3,7,5]
target = 11

print(subarraySum_v2(arr,target))