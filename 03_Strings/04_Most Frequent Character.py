"""
Given a string s of lowercase alphabets. 
The task is to find the maximum occurring character in the string s. 
If more than one character occurs the maximum number of times then print the lexicographically smaller character.

"""

def Most_Frequent_Character(s):

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    
    max_count = 0
    s2 = ""

    for ch in freq:
        if freq[ch] > max_count:
            max_count = freq[ch]
            s2 = ch
        elif freq[ch] == max_count:
            if ch < s2:
                s2 = ch

    return s2

s = "testsampale"
print(Most_Frequent_Character(s))



def Most_Frequent_Character_v2(s):

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    
    max_count = max(freq.values())
    s2 = []

    for ch in freq:
        if freq[ch] == max_count:
            s2.append(ch)

    ans = min(s2)
    return ans

s = "testsampale"
print(Most_Frequent_Character_v2(s))
