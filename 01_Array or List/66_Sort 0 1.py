def sortZeroesAndOne(arr, n) :
    # write your code here 
    k = 0

    for i in range(n):

        if arr[i] != 1:
            arr[k],arr[i] = arr[i],arr[k]
            k += 1

    return arr

    
n = 7
arr = [0,1,1,0,1,0,1]
print(sortZeroesAndOne(arr,n))