def anagram(word1,word2):

    if len(word1) != len(word2):
        return False
    
    return sorted(word1) == sorted(word2)


word1 = "rajas"
word2 = "ajras"

print(anagram(word1,word2))

from collections import Counter

def isAnagram( s, t):
        return Counter(s) == Counter(t)

s = "rajas"
t = "ajras"
print(isAnagram(s,t))

