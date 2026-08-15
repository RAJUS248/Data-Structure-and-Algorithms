def is_isomorphic(string1,string2):
    
    if len(string1) != len(string2):
        return False
    
    s1 = {}
    s2 = {}

    for c1,c2 in zip(string1,string2):
        if c1 in s1 and s1[c1] != c2:
            return False

        if c2 in s2 and s2[c2] != c1:
            return False
        
        s1[c1] = c2
        s2[c2] = c1

    return "true"
        
string1 = "badc"
string2 = "baba"

print(is_isomorphic(string1,string2))