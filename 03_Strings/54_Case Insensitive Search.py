def search(pat, txt):
    
    m = len(txt)
    n = len(pat)
    res = []
    for i in range(m-n+1):

        j = 0

        while j < n:

            if 'a' <= txt[i+j] <= 'z':
                ch1 = ord(txt[i+j]) - ord('a')

            elif 'A' <= txt[i+j] <= 'Z':
                ch1 = ord(txt[i+j]) - ord('A')

            else:
                break

            if 'a' <= pat[j] <= 'z':
                ch2 = ord(pat[j]) - ord('a')

            elif 'A' <= pat[j] <= 'Z':
                ch2 = ord(pat[j]) - ord('A')

            else:
                break


            if ch1 != ch2:
                break

            j += 1

        if j == n:
            res.append(i)

    return res


pat = "aB"
txt = "aBcAb"
print(search(pat,txt))



def search_v2(pat, txt):
    
    txt = txt.lower()
    pat = pat.lower()

    m = len(txt)
    n = len(pat)
    
    res = []
    
    for i in range(m-n+1):

        j = 0

        while j < n and txt[i+j] == pat[j]:
            j += 1

        if j == n:
            res.append(i)

    return res


pat = "aB"
txt = "aBcAb"
print(search_v2(pat,txt))



def search_v3(pat, txt):
    
    m = len(pat)
    n = len(txt)

    p = pat.lower()
    t = txt.lower()

    if m > n:
        return []

    lps = [0] * m
    length = 0
    i = 1

    while i < m:

        if p[i] == p[length]:

            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length-1]

            else:
                lps[i] = 0
                i += 1
    
    res = []
    i = 0
    j = 0

    while i < n:

        if p[j] == t[i]:
            i += 1
            j += 1

        if j == m:
            res.append(i-j)
            j = lps[j-1]

        elif i < n and p[j] != t[i]:

            if j != 0:
                j = lps[j-1]

            else:
                i += 1

    return res

pat = "aB"
txt = "aBcAb"
print(search_v3(pat,txt))


def search_v4(pat, txt):

    pat=pat.lower()
    txt=txt.lower()
    n=len(txt)
    #try with sliding window
    k=len(pat)
    i,j=0,k-1
    l=[]
 
    while j<n:
        # if j-i+1<k:
        #     j+=1
        if j-i+1==k:
            if txt[i:j+1]==pat:
                l.append(i)
            i+=1
            j+=1
    return l

pat = "aB"
txt = "aBcAbcab"
print(search_v4(pat,txt))