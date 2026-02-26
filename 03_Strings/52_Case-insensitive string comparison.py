def case_insensitive_string_comparison(s1,s2):

    if len(s1) != len(s2):
        return False
    
    if not s1 and not s2:
        return True
    
    index = 0

    while index < len(s1): # for index in range(len(s1))

        if 'a' <= s1[index] <= 'z':

            ch1 = ord(s1[index]) - ord('a')

        elif 'A' <= s1[index] <= 'Z':

            ch1 = ord(s1[index]) - ord('A')

        else:
            return False

        if 'a' <= s2[index] <= 'z':

            ch2 = ord(s2[index]) - ord('a')

        elif 'A' <= s2[index] <= 'Z':

            ch2 = ord(s2[index]) - ord('A')

        else:
            return False
        

        if ch1 != ch2:
            return False
        
        index += 1
        
    return True

s1 = 'car'
s2 = 'Cer'
print(case_insensitive_string_comparison(s1,s2))

