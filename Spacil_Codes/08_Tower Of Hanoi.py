def towerOfHanoi(n,src,aux,dest):
    # return (2**n)-1
    # return (1 << n) - 1
    
    if n == 0:
        return 0
    
    count = towerOfHanoi(n-1,src,dest,aux)
    count += 1
    count += towerOfHanoi(n-1,aux,src,dest)

    return count

print(towerOfHanoi(3,'a','b','c'))