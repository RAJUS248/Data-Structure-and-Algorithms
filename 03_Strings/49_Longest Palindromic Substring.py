def longestPalindrome(s):

    n = len(s)
    
    max_sub = ""

    for i in range(n):

        # for odd
        
        left = i
        right = i

        while left >= 0 and right < n and s[left] == s[right]:

            left -= 1
            right += 1

        if len(max_sub) < right - (left + 1):
            max_sub = s[left+1:right]

        # for even

        left = i
        right = i+1
        
        while left >= 0 and right < n and s[left] == s[right]:

            left -= 1
            right += 1

        if len(max_sub) < right - (left + 1):
            max_sub = s[left+1:right]

    return max_sub

s = "cbbd"
print(longestPalindrome(s))