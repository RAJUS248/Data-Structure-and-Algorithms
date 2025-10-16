def count_freq(arr):
    seen = {}

    for num in arr:
        if num in seen:
            seen[num] += 1

        else:
            seen[num] = 1

    print(seen)

arr = [1, 2, 2, 3, 1, 2]
count_freq(arr)

# using get()

def count_freq_v2(arr):
    seen = {}

    for num in arr:
        seen[num] = seen.get(num,0) + 1

    print(seen)

arr = [1, 2, 2, 3, 1, 2]
from collections import Counter
seen1 = Counter(arr)
print(seen1)
count_freq_v2(arr)