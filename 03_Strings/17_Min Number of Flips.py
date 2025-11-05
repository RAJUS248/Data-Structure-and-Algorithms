def min_flip(s):

    count1 = 0
    count2 = 0

    for i in range(len(s)):
        
        if i % 2 == 0:
            expected_for_0 = '0'  
        
        else:
            expected_for_0 = '1'

        if i % 2 == 0:
            expected_for_1 = '1'

        else:
            expected_for_1 = '0'  


        if s[i] != expected_for_0:
            count1 += 1

        if s[i] != expected_for_1:
            count2 += 1

    return min(count1,count2)


s = "0001010111" 
print(min_flip(s))


def min_flip_v2(s):
    count0 = 0   # flips if pattern starts with '0'
    count1 = 0   # flips if pattern starts with '1'

    pattern = {}   # we'll use dict to store what each index should be

    for i in range(len(s)):
        if i % 2 == 0:
            pattern[i] = ('0', '1')   # (expected if start=0, expected if start=1)
        else:
            pattern[i] = ('1', '0')

    for i in range(len(s)):
        if s[i] != pattern[i][0]:   # compare with pattern starting with '0'
            count0 += 1
        if s[i] != pattern[i][1]:   # compare with pattern starting with '1'
            count1 += 1

    return min(count0, count1)

s = "0001010111" 

print(min_flip_v2(s))