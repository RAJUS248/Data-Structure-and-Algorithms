def majority(arr):
    freq = {}
    length = len(arr)
    N = length/2
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1   # .get(num, 0) → checks if num exists in freq. If yes, returns its count; otherwise, returns 0.Add 1 to increment the count. After processing arr = [2, 2, 1, 1, 1, 2, 2] → freq = {2: 4, 1: 3}

    most_repeated = max(freq, key=freq.get)  # find number with max frequency
    count = freq[most_repeated] 
    
    if count > N:
        print(most_repeated)

    else:
        print("No majority element")
# arr = [2,2,1,1,3,2,2,1,1,2,3,2,1,1]
# majority(arr)

# wonderful

def majority_boyer_moore_debug(arr):
    candidate = None
    counts = 0

    for num in arr:

        if counts == 0:
            candidate = num
            counts = 1

        elif num == candidate:
            counts += 1

        else:
            counts -= 1

    if arr.count(candidate) > len(arr)/2:
         print("Majority element:", candidate)
    else:
        print("No majority element")

arr =  [1,1,1,1,1,1,2,2,2,3,3]
majority_boyer_moore_debug(arr)

arr = [1,1,2,3,4,1,5,6,2,2,3]


