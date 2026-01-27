from collections import Counter
def create_mountain(arr):

    n = len(arr)

    h = []
    for i in range(n):
        left = i
        right = n - 1 - i
        h.append(min(left,right))

    need = []

    for i in range(n):
        need.append(arr[i] - h[i])
        
    freq = Counter(need)

    max_keep = 0

    for value in freq.values():

        if value > max_keep:
            max_keep = value

    return n - max_keep
    

arr = [1,3,1]
print(create_mountain(arr))