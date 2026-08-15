def two_sum(arr,target):
    seen = {}

    for index, num in enumerate(arr):

        sec_num = target - num

        if sec_num in seen:
            return seen[sec_num],index

        seen[num] = index

arr = [2,7,11,15,15,7,2,10]
target = 25
print(two_sum(arr,target))