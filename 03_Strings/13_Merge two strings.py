def merge(s1,s2):

    length = max(len(s1),len(s2))
    res = ""
    
    for i in range(length):

        if i < len(s1):
            res += s1[i]

        if i < len(s2):
            res += s2[i]

    return res

s1 = "Hello" 
s2 = "Bye"
print(merge(s1,s2))