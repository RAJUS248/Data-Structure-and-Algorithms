def palindrome(string):

    start = 0
    end = len(string) - 1

    while start < end:  
        if string[start] != string[end]:   
            return False
        start += 1
        end -= 1

    return True
print(palindrome("mamaamam"))
        
def palindrome_v2(string):

    return string == string[::-1]

print(palindrome_v2("mada"))

        

