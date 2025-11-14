def Triplets_Smaller_Sum(n,sums,arr):
    
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):

                if arr[i] + arr[k] + arr[j] < sums:

                    count += 1

    return count

n = 5
sums = 12
arr = [5, 1, 3, 4, 7]

print(Triplets_Smaller_Sum(n,sums,arr))


def Triplets_Smaller_Sum_v2(n,sums,arr):
    
    arr.sort()
    count = 0

    for i in range(n-2):

        left = i + 1
        right = n - 1

        while left < right:

            if arr[i] + arr[left] + arr[right] < sums:

                count += right - left
                left += 1

            else:
                right-= 1

    return count

n = 5
sums = 12
arr = [5, 1, 3, 4, 7]

print(Triplets_Smaller_Sum_v2(n,sums,arr))



