def two_sum(arr,target):

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                
                print(i,j)
         

arr = [1,3,2,5,6]
target = 5
two_sum(arr,target)

def two_sum_v2(arr,target):

    seen = {}

    for index,num in enumerate(arr):
        sec_num = target - num
        if sec_num in seen:
            print(seen[sec_num],index)

        seen[num] = index
     

arr = [2,3,2,5,7]
target = 8
two_sum_v2(arr,target)



