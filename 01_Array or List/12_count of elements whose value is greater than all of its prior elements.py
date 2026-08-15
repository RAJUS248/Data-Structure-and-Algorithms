def count_greater_prior(arr):
    count = 0
    maxi = float("-inf")
    for i in range(len(arr)):

        if arr[i] > maxi:
            count += 1
            maxi = arr[i]

    print(count)

arr = [7,4,8,2,9,10]
count_greater_prior(arr)

# or

def count_greater_prior_v2(arr):
    count = 0
    max_so_far = float('-inf')  # initial max as very small number
    
    for num in arr:
        if num > max_so_far:
            count += 1
            max_so_far = num  # update max
    
    print(count)

arr = [7, 4, 8, 2, 9]
count_greater_prior_v2(arr)  # Output: 3
