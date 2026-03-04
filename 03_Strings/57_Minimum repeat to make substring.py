
def minRepeats_v2(s1, s2):

    m = len(s1)
    n = len(s2)

    
    count = (m+n-1) // m
    
    s = s1 * count

    if s2 in s:

        return count
    
    s += s1
    count += 1

    if s2 in s:
        return count

    return -1

s1 = "abac"
s2 = "cabaca" 
print(minRepeats_v2(s1,s2))


def minRepeats(s1, s2):

    s = s1
    count = 1
    for _ in range((len(s2)//len(s1))+1):

        if s2 not in s:
            s += s1
            count += 1

    if s2 in s:

        return count

    return -1

s1 = "abac"
s2 = "cabaca" 
print(minRepeats(s1,s2))