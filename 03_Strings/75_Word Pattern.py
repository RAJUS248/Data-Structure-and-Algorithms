def wordPattern(pattern, s):
        
        words = s.split()

        if len(pattern) != len(words):
            return False


        chr_words = {}
        words_chr = {}

        for c,w in zip(pattern,words):
            
            if c in chr_words and chr_words[c] != w:
                return False
            
            if w in words_chr and words_chr[w] != c:
                return False
            
            chr_words[c] = w      
            words_chr[w] = c

            
        return True
                

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern,s))


