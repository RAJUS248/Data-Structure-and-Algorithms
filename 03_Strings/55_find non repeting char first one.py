def find_non_repeting_char_first_one(s):

    seen = {}
   

    for ch in s:
        seen[ch] = seen.get(ch,0) + 1

    for ch in s:
        if seen[ch] == 1:
            return ch

        
s = 'swiss'
print(find_non_repeting_char_first_one(s))