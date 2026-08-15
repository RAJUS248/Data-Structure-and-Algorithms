arr = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7

count = 0
for i in range(len(arr)):
    total = 0
    for j in range(i, len(arr)):
        total += arr[j]
        if total == k:
            count += 1
print(count)

def subarray_sum_v2(arr,k):
    total = 0
    count = 0
    seen = {}

    for num in arr:
        total += num

        if total == k:
            count += 1
        sec_num = total - k
        if sec_num in seen:
            count += seen[sec_num]

        seen[total] = seen.get(total,0) + 1

    print(count)

arr = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7

subarray_sum_v2(arr,k)