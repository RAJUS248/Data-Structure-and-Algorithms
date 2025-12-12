def first_all(s):

    if s is None:
        return ""
    
    letr = ""
    num = ""
    prev = s[0]

    if prev.isalpha():
        letr += prev

    else:
        num += prev

    for i in range(1,len(s)):
        
        cur = s[i]

        if ( cur.isalpha() and prev.isdigit() ) or (cur.isdigit() and prev.isalpha()):

            if cur.isalpha():
                letr += s[i]

        
            else:
                num += s[i]

        prev = cur

    return letr + num

s = "ABC120PME0000LZ3MB1Y3C45"
print(first_all(s))