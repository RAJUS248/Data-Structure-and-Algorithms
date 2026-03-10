def sortVowels(s):
   
    lst = list(s)
    seen = {'a','e','i','o','u','A','E','I','O','U'}
    
    for i in range(len(s)): 
        if lst[i] not in seen: 
            continue 
        for j in range(i+1,len(s)): 
            if lst[i] in seen and lst[j] in seen: 
                if ord(lst[i]) > ord(lst[j]): 
                    lst[i],lst[j] = lst[j],lst[i] 
    
    return ''.join(lst)

s = "UpjPbEnOj"
print(sortVowels(s))



def sortVowels_v2(s):
   
    lst = list(s)
    seen = {'a','e','i','o','u','A','E','I','O','U'}

    vowels = []

    for ch in s:
        if ch in seen:
            vowels.append(ch)

    vowels.sort()
    j = 0
    for i in range(len(lst)):
        if lst[i] in seen:
            lst[i] = vowels[j]
            j += 1
        
    return ''.join(lst)
    
s = "UpjPbEnOj"
print(sortVowels_v2(s))


 

 