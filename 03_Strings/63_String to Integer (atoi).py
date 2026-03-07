def myAtoi(s):
    
    n = len(s)
    int_max = (2**31)-1
    int_min = -2**31
    i = 0
    res = 0
    sign = 1

    while i < n and s[i] == ' ':
        i += 1

    
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1

        i += 1

    while i < n and s[i].isdigit():

        if res > (int_max - int(s[i])) // 10:

            if sign == 1:
                return int_max
            else:
                return int_min
        
        res = res * 10 + int(s[i])

        i += 1

    return res * sign


s = "++1"
print(myAtoi(s))