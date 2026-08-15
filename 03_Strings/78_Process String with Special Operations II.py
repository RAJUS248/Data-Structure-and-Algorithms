def processStr(s, k):
    
    l = 0

    for c in s:
        
        if c == "*" and l > 0:
            l -= 1
        
        elif c == "#":
            l *= 2

        elif c.isalpha():
            l += 1
    
    if k >= l:
        return "."

        
    for i in range(len(s)-1,-1,-1):

        c = s[i]

        if c == "*":
            l += 1

        elif c == "#":
            l = l//2

            if k >= l:
                k -= l

        elif c == "%":
            k = l - 1 - k

        else:
            if k == l - 1:
                return c
            
            l -= 1

    return "."
    

        
        
s = "cd%#*#"
k = 3
print(processStr(s,k))