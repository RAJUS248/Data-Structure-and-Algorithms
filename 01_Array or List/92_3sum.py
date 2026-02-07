def three_sum_v3(arr):

    n = len(arr)
    arr.sort()
    res = []
    
    for i in range(n):

        left = i + 1
        right = n - 1
        the_sum = 0

        if arr[i] > 0:
            break

        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        while left < right:

            the_sum = arr[i] + arr[left] + arr[right]

            if the_sum == 0:
    
                res.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left-1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1


            elif the_sum < 0:
                left += 1

            else:
                right -= 1

    return res
        

arr = [-1,0,1,2,-1,-4]
print(three_sum_v3(arr))