def numberOfSpecialChars(word):
        
        seen = {}
        s = set(word)
        for i in range(len(word)):

            if word[i].islower():
                seen[word[i]] = i

            if word[i].isupper() and word[i] not in seen:
                seen[word[i]] = i

        count = 0
        for ch in s:
            uper = ch.upper()
            if uper in seen and seen[ch] < seen[uper]:
                count += 1

        return count 

word = "aaAbcBC"
print(numberOfSpecialChars(word))