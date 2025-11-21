def URLify(s):

    s = list(s)

    for i in range(len(s)):
        if s[i] == " ":
            s[i] = "%20"

    return "".join(s)

s = "i love programming"
print(URLify(s))


def URLify_v2(s,n):

    space_count = 0
    for i in range(n):
        if s[i] == " ":
            space_count += 1

    new_indx = (n + space_count * 2) -1

    for i in range(n-1,-1,-1):
        if s[i] == " ":
            s[new_indx] = "0"
            s[new_indx-1] = '2'
            s[new_indx-2] = '%'
            new_indx -= 3

        else:
            s[new_indx] = s[i]
            new_indx -= 1

    return s


# s = ["M","r"," ","J","o","h","n"," ","S","m","i","t","h","","","",""]
s = ['r','s',' ','b','','']
n = 4 
print(URLify_v2(s,n))