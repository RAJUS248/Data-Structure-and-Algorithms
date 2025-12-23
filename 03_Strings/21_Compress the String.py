def getCompressedString(s):

    res = ''
    str_count = 1

    for i in range(1,len(s)):

        if s[i] == s[i-1]:

            str_count += 1

        else:
            if str_count == 1:
                res += s[i-1]

            else:
                res += s[i-1] + str(str_count)
            
            str_count = 1

    if str_count == 1:
        res += s[-1]

    else:
        res += s[-1] + str(str_count)
        
    return res

s = 'aaabbccdsa'
print(getCompressedString(s))
