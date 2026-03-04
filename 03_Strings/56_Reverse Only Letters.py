def reverseOnlyLetters(s):

    n = len(s)
    res = ''
    i = 0
    j = n-1

    while i < n and j >= 0:

        if s[i].isalpha() and s[j].isalpha():
            res += s[j]
            i += 1
            j -= 1
        
        elif not s[i].isalpha():
            res += s[i]
            i += 1

        if not s[j].isalpha():
            j -= 1
        
    if i == n-1 or j <= n:
        return res + s[i:]
    
    return res

    
s = "ab-cd"# "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(s))



def reverseOnlyLetters_v2(s):

    n = len(s)
    s = list(s)
    i = 0
    j = n-1

    while i < j:

        if not s[i].isalpha():
            i += 1

        elif not s[j].isalpha():
            j -= 1

        else:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
    
    
    return "".join(s)

    
s = "ab-cd"# "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters_v2(s))