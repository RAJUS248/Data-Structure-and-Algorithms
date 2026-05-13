def sumOddLengthSubarrays(arr):
        
        odd_sum = 0

        for j in range(1,len(arr)+1,2):

            for i in range(len(arr)):  

                if j+i < len(arr)+1:
                    odd_sum += sum(arr[i:j+i])

                else:
                    break

        
        return odd_sum

arr = [1,2] #[1,4,2,5,3,8]
print(sumOddLengthSubarrays(arr))


def sumOddLengthSubarrays_v2(arr):
     
    n = len(arr)
    start = n
    end = 1

    odd_len_sum_subarray = 0
    for i in range(n):
        
        total = start * end
        odd_len_sum_subarray += arr[i] * ((total + 1) // 2)  # for even no add 1 for odd total add 1 but for // 2 it convert no change

        start -= 1
        end += 1

    return odd_len_sum_subarray

arr = [1,4,2,5,3]
print(sumOddLengthSubarrays_v2(arr))