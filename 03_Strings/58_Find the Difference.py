def findTheDifference(s, t):

    s = sorted(s)
    t = sorted(t)

    for i in range(len(s)):

        if s[i] != t[i]:
            return t[i]
        
    return t.pop() 
        
s = "abcd"
t = "abcde"
print(findTheDifference(s,t))


def findTheDifference_v2(s, t):

    ans = 0

    for ch in t:
        ans ^= ord(ch)

    for ch in s:
        ans ^= ord(ch)

    return chr(ans)
       
s = "abcd"
t = "abcde"
print(findTheDifference_v2(s,t))
