def removeAnagrams(words):

    res = [words[0]]
    for i in range(1,len(words)):

        if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])
       
        
    return res

def removeAnagrams_v2(words):
     
    def count_char(word):
         
        count = [0] * 26

        for ch in word:
            
            count[ord(ch) - ord('a')] += 1

        return count
    
    result = [words[0]]
    prev_count = count_char(words[0])
    
    for i in range(len(words)):
        cur_count = count_char(words[i])

        if prev_count != cur_count:
            result.append(words[i])
            prev_count = cur_count

    return result
        

words = ["abba","baba","bbaa","cd","cd"]
print(removeAnagrams(words))
print(removeAnagrams_v2(words))