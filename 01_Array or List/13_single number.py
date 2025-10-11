arr = [1,2,1,2,3]
freq = {}

for num in arr:
    if num in freq:
         freq[num] += 1
        
    else:
        freq[num] = 1
        
for num, count1 in freq.items():
    if count1 == 1:
        print(num)


# its magic for only repeted twice numbers
arr = [1,2,1,2,3]

res = 0
for num in arr:
    res ^= num

print(res)