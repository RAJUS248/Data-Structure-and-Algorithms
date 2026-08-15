def countCharacters(words, chars):
        
        length = 0
        
        for word in words:

            valid = True
            lst_chars = list(chars)
            for c in word:

                if c not in lst_chars:
                    valid = False
                    break

                else:
                    lst_chars.remove(c)

            
            if valid:
                length += len(word)

        return length

words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters(words,chars))


def countCharacters_v2(words, chars):
        
        length = 0

        for ch in words:
            valid = True

            for c in ch:
                
                if ch.count(c) > chars.count(c):
                    valid = False
                    break
            
            if valid:
                length += len(ch)
        
        return length

words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters_v2(words,chars))


from collections import Counter
def countCharacters_v3(words, chars):
        
        length = 0
        chars_count = Counter(chars)

        for word in words:
            word_count = Counter(word)
            
            valid = True
            for ch in word_count:
                
                if word_count[ch] > chars_count[ch]:
                    valid = False
                    break

            if valid:
                length += len(word)
            
        return length

words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters_v3(words,chars))