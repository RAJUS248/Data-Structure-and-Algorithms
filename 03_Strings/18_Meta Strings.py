def Meta_Strings(s1,s2):

    if s1 == s2 or len(s1) != len(s2):
        return 0
    
    lst = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            lst.append(i)

    if len(lst) == 2:
      i,j = lst[0],lst[1]

      if s1[i] == s2[j] and s2[i] == s1[j]:
          
        return 1
  
    return 0
           

s1 = "geeks"
s2 = "keges"

print(Meta_Strings(s1,s2))

