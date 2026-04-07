def removeConsecutiveDuplicates(string):
    
    res = ''
    res += string[0]
    for i in range(1,len(string)):

        if string[i-1] != string[i]:
            res += string[i]

    return res  

string = 'xxxyyyzwwzzz'
print(removeConsecutiveDuplicates(string))
 

# recurcive

def removeConsecutiveDuplicates_v2(string):
    
    if len(string) <= 1:
        return string
    

    if string[0] == string[1]:
        return removeConsecutiveDuplicates_v2(string[1:])

    else:
        return string[0] + removeConsecutiveDuplicates_v2(string[1:])

string = 'xxxyyyzwwzzz'
print(removeConsecutiveDuplicates_v2(string))
