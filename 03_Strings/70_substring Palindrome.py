def substring_palindrome(s:str):

    def is_palindeome(strs):

        return strs == strs[::-1]


    for i in range(len(s)):
        for j in range(1,len(s)):

            str1 = s[i:]
            str2 = s[i:j]
            str3 = s[j:]

            if is_palindeome(str1) and is_palindeome(str2) and is_palindeome(str3):

                print(str1)
                print(str2)
                print(str3)

                return


s = 'nayannamantenet'
substring_palindrome(s)