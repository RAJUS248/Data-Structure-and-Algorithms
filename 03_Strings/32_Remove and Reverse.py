def Remove_and_Reverse(s):
    seen = {}
    for ch in s:
        seen[ch] = seen.get(ch,0) + 1

    i = 0
    j = len(s) - 1
    front = True
    pos = set()

    while i <= j:
        
        if front == True:
            if seen[s[i]] > 1:
                front = False
                seen[s[i]] -= 1
            
            else:
                seen[s[i]] == 1
                pos.add(i)

            i += 1

        else:
            if seen[s[j]] > 1:
                front = True
                seen[s[j]] -= 1
            
            else:
                seen[s[j]] == 1
                pos.add(j)

            j -= 1


    res = ""
    for k in range(len(s)):

        if k in pos:
            res += s[k]

    if front == False:
        res = res[::-1] 

    return res

s = "cababcea"
print(Remove_and_Reverse(s))
