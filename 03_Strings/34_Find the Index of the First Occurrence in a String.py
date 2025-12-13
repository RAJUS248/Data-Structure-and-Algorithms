def strStr(haystack, needle):
    l = len(needle)

    for i in range(len(haystack)-l+1):

        if haystack[i : i + l] == needle:
            return i
        
    return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack,needle))