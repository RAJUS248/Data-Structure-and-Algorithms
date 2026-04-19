def cumulative_sum(n,arr):

    arr1 = arr.copy()
    arr2 = arr.copy()

    for i in range(1,n):
        arr1[i] = arr1[i-1] + arr1[i]

    orginal_arr = arr2[::-1]
    for j in range(1,n):
        orginal_arr[j] = orginal_arr[j-1] + orginal_arr[j]

    return arr,arr1,orginal_arr


n = int(input('Please enter no. of elements: '))
arr = list(map(int,input('Please enter arr elements: ').split()))

if len(arr) != n:
    print('enter correct no. of elements')

else:
    print(cumulative_sum(n,arr))