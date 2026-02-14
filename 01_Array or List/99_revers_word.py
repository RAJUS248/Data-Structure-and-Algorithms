def reverse_string(s):

    i = 0
    res = ""
    for j in range(len(s)):

        if s[j] == ' ' or s[j] == '\t':

            if i < j:
                res += s[i:j][::-1] + ' '
            i = j+1

    res += s[i:j+1][::-1]
    return res.strip()[::-1]

def reverseWords(s):

    lst = s.strip()
    l = list(map(str,lst.split()))
    res = ""

    for i in range(len(l)-1,-1,-1):

        res += l[i] + " "
    
    return res.strip()

def revers_word(s):

    lst = s.split()
    # return " ".join(reversed(lst))

    res = ''
    for i in range(len(lst)-1,-1,-1):
        res += lst[i] + ' '

    return res.strip()


s = '    the sky   is blue   '
print(reverse_string(s))
print(reverseWords(s))
print(revers_word(s))
