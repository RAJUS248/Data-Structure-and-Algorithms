def dublicate(arr):
    seen = {}
    for num in arr:
        
        seen[num] = seen.get(num,0) + 1

    for k,v in seen.items():

        if v > 1:
            print(k)

arr = [1, 2, 2, 3, 1, 4]
dublicate(arr)

def dublicate_v2(arr):
    seen = {}
    dublicate = []
    for num in arr: 
        if num in seen:
            seen[num] += 1

            if seen[num] == 2:
                dublicate.append(num)

        else:
            seen[num] = 1
    
    print(dublicate)

arr = [1, 2, 2, 3, 1, 4,1,1]
dublicate_v2(arr)



