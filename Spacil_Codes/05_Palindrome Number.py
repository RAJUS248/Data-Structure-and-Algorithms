def isPalindrome(x):

    if x < 0:
        return False
    
    original = x
    rev_num = 0
    while x > 0:
        last_digit = x % 10
        rev_num = (rev_num * 10) + last_digit
        x = x // 10

    return original == rev_num
    
x = 101
print(isPalindrome(x))



# or

def isPalindrome_v2(x):

    if x < 0 or (x % 10 == 0 and x != 0): # the number end with 0 like 120,20,10 it will detect
        return False
    
    rev_num = 0
    while x > rev_num:
        last_digit = x % 10
        rev_num = (rev_num * 10) + last_digit
        x = x // 10

    return x == rev_num or x == rev_num // 10  # odd and even x ex : 12321 123 // 10 = 12 
    
x = 1013
print(isPalindrome_v2(x))