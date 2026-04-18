def rotate_array(arr,d):

    n = len(arr)

    d = d % n

    def reverse(left,right):
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1

    reverse(0,d-1)

    reverse(d,n-1)

    reverse(0,n-1)

    return arr

arr = [1,2,3,4,5]
d = 2
print(rotate_array(arr,d))