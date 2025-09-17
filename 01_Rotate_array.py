def rotate_array(arr, k):
    n = len(arr)
    k = k % n   # handle if k > n
    
    # Step 1: reverse whole array
    arr.reverse()
    
    # Step 2: reverse first k elements
    arr[:k] = reversed(arr[:k])
    
    # Step 3: reverse remaining n-k elements
    arr[k:] = reversed(arr[k:])
    
    return arr

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated array:", rotate_array(arr, k))


def arr_rotate(arr,k):
    n =  len(arr)
    k %= n

    def reverse(start,end):
        while start < end :
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1

    # Step 1: reverse whole array
    reverse(0,n-1)

    # Step 2: reverse first k
    reverse(0,k-1)

     # Step 3: reverse rest
    reverse(k,n-1)

    print(arr)

arr = [1,2,3,4,5,6,7,8]
k = 3
arr_rotate(arr,k)

 # Time Complexity: O(n)

# Space Complexity: O(1)
