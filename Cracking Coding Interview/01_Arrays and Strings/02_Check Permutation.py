"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other

"""
from collections import Counter
def Check_Permutation_v2(string1,string2):

    if len(string1) != len(string2):
        return False
    
    return Counter(string1) == Counter(string2)


string1 = "aabc"
string2 = "baac"

print(Check_Permutation_v2(string1,string2))



def Check_Permutation(string1,string2):

    if len(string1) != len(string2):
        return False
    
    seen = {}

    for chr in string1:
        seen[chr] = seen.get(chr,0) + 1

    for chr2 in string2:
        if chr2 not in seen:
            return False
        
        seen[chr2] -= 1

        if seen[chr2] < 0:
            return False
        
    return True


string1 = "aabc"
string2 = "baaa"

print(Check_Permutation(string1,string2))



def Check_Permutation_v3(string1,string2):

    if len(string1) != len(string2):
        return False
    
    return sorted(string1) == sorted(string2)


string1 = "aabcf"
string2 = "baacd"

print(Check_Permutation_v3(string1,string2))
