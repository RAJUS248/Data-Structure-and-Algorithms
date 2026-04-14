def linear_search(arr,key):

    for num in arr:

        if num == key:
            return 'Key is present'
        
    return 'Key is not present'
    
arr = [9,4,7,6,8,1,8,3,7,2] 
key = 10
result = linear_search(arr,key)

print(result)
