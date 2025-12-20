def isRepeat(s):
    
    double = s + s

    search = double[1:-1]

    if s in search:
        return 1
    else:
        return 0

s = "ababab"
print(isRepeat(s))