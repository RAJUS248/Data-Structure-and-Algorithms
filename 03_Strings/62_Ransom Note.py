def canConstruct(ransomNote, magazine):
        
        magazine = list(magazine)
        for ch in ransomNote:
            if ch not in magazine:
                return False

            magazine.remove(ch)
            
        return True

def canConstruct_v2(ransomNote, magazine):
     
    for ch in ransomNote:
            if ch not in magazine:
                return False
            
            magazine = magazine.replace(ch,'',1)

    return True
     
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote,magazine))
print(canConstruct_v2(ransomNote,magazine))