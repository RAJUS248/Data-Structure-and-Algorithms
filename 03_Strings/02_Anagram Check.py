def Anagram_Check(string1,string2):

    return sorted(string1) == sorted(string2)

print(Anagram_Check("raja","ajar"))


def Anagram_Check_v2(string1,string2): 

    freq = {}
    freq1 = {}
    
    for ch in string1:
        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] = 1
    
    for ch in string2:
        if ch in freq1:
           freq1[ch] += 1

        else:
            freq1[ch] = 1
   
    return freq == freq1

print(Anagram_Check_v2("raja","ajaj"))


def Anagram_Check_v3(string1,string2):

    freq = {}
    
    for ch in string1:
        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] = 1
    
    for ch in string2:
        if ch not in freq:
           return False
        freq[ch] -= 1

        if freq[ch] < 0:
            return False
        
    
    return True


print(Anagram_Check_v3("raja","xyz"))
