def isPalindrome(s):
    i = 0
    j = len(s) - 1

    s = s.lower()
    
    while i < j:
        if s[i].isalnum() and s[j].isalnum():
            if s[i] == s[j]:
                i += 1
                j -= 1

            else:
                return False
        
        elif not s[i].isalnum():
            i += 1

        else:
            j -= 1

    return True
    

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

# or

def isPalindrome_v2(s):
    i = 0
    j = len(s) - 1

    s = s.lower()
    
    while i < j:

        if not s[i].isalnum():
            i += 1

        elif not s[j].isalnum():
            j -= 1

        else:

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

    return True
    

s = "A man, a plan1, a ca1nal: Panama"
print(isPalindrome_v2(s))