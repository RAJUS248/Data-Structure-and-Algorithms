def plusMinus(arr) -> float:
    # Write your code here
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range (len(arr)):
        if arr[i] > 0:
            count1 +=1
            continue
        if arr[i] < 0:
            count2 +=1
            continue
        if arr[i] == 0:
            count3 +=1
            continue
    return count1 / len(arr), count2 / len(arr), count3 / len(arr)
        
        
arr = [1,1,-2,-2,0]

print("div is" , plusMinus(arr))