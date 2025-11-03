def longest_prefix_string(s):

    if not s:
        return ""

    refr_word = s[0]
    for i in range(len(refr_word)):
        
        chr_to_check = refr_word[i]

        for j in range(1,len(s)):

            cur_word = s[j]

            if i >= len(refr_word) or chr_to_check != cur_word[i]:

                return refr_word[:i]

    return refr_word

s = ["geeksforgeeks", "geezer", "geek", "geeks"]
print(longest_prefix_string(s))



def longestCommonPrefix(arr):
        # code here
        arr.sort()
        print(arr)
        a = arr[0]
        b = arr[-1]
        l = min(len(a), len(b))
        res = ""
        for i in range(l):
            if a[i] != b[i]:
                return res
            res += a[i]

        
        return res

arr = ["geeksforgeeks", "eezer", "eek", "eeks"]

print(longestCommonPrefix(arr))