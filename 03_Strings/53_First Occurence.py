def firstOccurence(txt,pat):

    m = len(txt)
    n = len(pat)

    for i in range(m-n+1):
        
        j = 0

        while j < n and  txt[i+j] == pat[j]:
            j += 1
       

        if j == n:
            return i
        
    return -1


txt = "geeksforgeeks"
pat = "fr"
print(firstOccurence(txt,pat))