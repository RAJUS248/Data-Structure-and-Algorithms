def first_non_rep(arr):
    for i in range(len(arr)):
        is_unique = True
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                is_unique = False
                break
        if is_unique:
            return arr[i]

arr = [9, 4, 9, 6, 7, 4]
print(first_non_rep(arr))


def first_non_rep_v2(arr):
    seen = {}

    for num in arr:
        if num in seen:
            seen[num] += 1

        else:
            seen[num] = 1

    for num in arr:
        if seen[num] == 1:
            return f"the key value is {num} and the count is {seen[num]}"
        
    """
    for key,value in (seen.items()):
        if value == 1:
            return f"the key is {key} and the count is {value}"
    """

arr = [9, 4, 9, 6, 7, 4]
print(first_non_rep_v2(arr))


from collections import Counter
def first_non_rep_v3(arr):
    counter = Counter(arr)
    for num in counter:
        if counter[num] == 1:
            return num

arr = [9, 4, 9, 6, 7, 4]
print(first_non_rep_v3(arr))


