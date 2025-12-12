def transform(A, B):

    if len(A) != len(B):
        return -1
    
    seen = {}

    for ch in A:
        seen[ch] = seen.get(ch,0) + 1

    for ch in B:
        seen[ch] = seen.get(ch,0) - 1

    for ch in seen:
        if seen[ch] != 0:
            return -1
        
    
    i = len(A) - 1
    j = len(B) - 1 

    count = 0
    while i >= 0 and j >= 0:

        if A[i] == B[j]:
            
            i -= 1
            j -= 1

        else:
            count += 1
            i -= 1
            
    return count


A = "abd"
B = "bad"
print(transform(A,B))