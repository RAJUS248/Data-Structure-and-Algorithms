def missing_num(arr):
    n = len(arr)

    total = n * (n + 1)//2

    actual_sum = sum(arr)

    return abs(total - actual_sum)

arr = [0,3,1]          # it means the missing number is 2  like 0,1,2,3 like this -> N

print(missing_num(arr))


def xor(arr):
    xor_full = 0
    xor_arr = 0

    for i in range(len(arr) + 1):
        xor_full ^= i

    for num in arr:
        xor_arr ^= num

    return xor_full ^ xor_arr

arr = [0,1,3,4,6] 
print(xor(arr))


def find_missing(arr):
    n = max(arr)   # or len(arr) + number of missing
    full_set = set(range(n+1))
    missing = full_set - set(arr)
    return sorted(list(missing))

arr = [0,2]
print(find_missing(arr))  # [2, 5]

def miss(arr):
    n = max(arr)
    set_arr = set(arr)

    missing = []

    for i in range(n+1):
        if i not in set_arr:
            missing.append(i)

    return missing
    
arr = [0,7]
print(miss(arr))

