def Anagram_of_String(s1,s2):

    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch,0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch,0) + 1

    
    all_chr = set(freq1.keys()|freq2.keys())

    delition = 0
    for ch in all_chr:
        delition += abs(freq1.get(ch, 0) - freq2.get(ch, 0))

    return delition

    

s1 = "abc"
s2 = "cde"


print(Anagram_of_String(s1,s2))
