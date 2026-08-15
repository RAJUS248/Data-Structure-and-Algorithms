def Character_Counter(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] = 1

    return freq

s = "hello world"
print(Character_Counter(s))

# or

from collections import Counter

def Character_Counter_v2(s):
    return Counter(s)

s = "hello world"
print(Character_Counter_v2(s))