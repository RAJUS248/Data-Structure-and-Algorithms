def roman_to_int(s):

    seen = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    total = seen[s[-1]]
    
    for i in range(len(s)-2,-1,-1):
        
        cur_val = seen[s[i]]
        cur_next_val = seen[s[i+1]]

        if cur_val < cur_next_val:

            total -= cur_val

        else:
            total += cur_val

    return total
            
s = "MCMIV"

print(roman_to_int(s))


def roman_to_int_v2(s):

    seen = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    total = 0
    
    for i in range(len(s)):

        if i+1 < len(s) and seen[s[i]] < seen[s[i+1]]:

            total -= seen[s[i]]

        else:
            total += seen[s[i]]

    return total
            
s = "MCMIV"

print(roman_to_int_v2(s))



