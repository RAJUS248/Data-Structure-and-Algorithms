def findEquilibrium(arr):
        # code here

        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            right_sum = total_sum - left_sum - arr[i]

            if left_sum == right_sum:
                  
                return i
            
            left_sum += arr[i]

        return -1

arr = [1,2,0,3]

print(findEquilibrium(arr))



def findEquilibrium_v2(arr):
        
        if len(arr) == 1:
            return arr[0]
        
        if len(arr) == 2:
            return -1
         

        
        sum_of_arr = [arr[0]]

        for i in range(len(arr)-1):
            sum_of_arr.append(sum_of_arr[i]+arr[i+1])

        for i in range(len(arr)):
            l_sum = sum_of_arr[i] - arr[i]
            r_sum = sum_of_arr[-1] - sum_of_arr[i]

            if l_sum == r_sum:
                 return i


        return -1

arr = [1,2,0,3]

print(findEquilibrium_v2(arr))