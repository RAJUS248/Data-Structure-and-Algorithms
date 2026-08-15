"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. 
Given two strings, write a function to check if they are
one edit (or zero edits) away.

"""

def one_away(string1,string2):

    # case 1: checking length

    if abs(len(string1) - len(string2)) > 1:
        return False
    
    # case 2: if length is same

    if len(string1) == len(string2):
        count_diff = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count_diff += 1

                if count_diff > 1:
                    return False
                
        return True

    # case 3: length is not same but only 1 diff length

    if len(string1) > len(string2):

        longer,shorter = string1,string2

    else:

        longer,shorter = string2,string1

    count = 0
    i = j = 0

    while i < len(longer) and j < len(shorter):

        if longer[i] != shorter[j]:
            count += 1
            
            if count > 1:
                return False
            
            i += 1
        else:   
            i += 1
            j += 1

    return True

    
string1 = "aacbb" 
string2 = "bb"

print(one_away(string1,string2))