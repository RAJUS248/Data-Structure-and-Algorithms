def getLPSLength(s):

    n = len(s)

    if n == 0:
        return 0
    
    p = 0
    i = 1

    while i < n:

        if s[p] == s[i]:

            p += 1

            i += 1

        else:
            if p != 0:
                p = 0
                # p = lps[p - 1]

            else:

                # lps[i] = 0
                
                i += 1

        
    return p

s = "ddbbbbcddd"
print(getLPSLength(s))


def pre_suf(s):

    n = len(s)
    n1 = len(s)
    i = 1
    while n > 0 :
        if s[0:n-1] == s[i:n1]:
            print(s[i:n1])
            return len(s[i:n1])
    
        n -= 1
        i += 1

s = "bcebcdbce"
print(pre_suf(s))

