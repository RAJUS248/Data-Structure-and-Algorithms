def generateNextPalindrome(num, n ):

    lst = []
    lst2 = lst
    
    for i in range(n//2):
        lst.append(num[i])

    res = lst + lst2[::-1]

    return res


n = 11
num = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
print(generateNextPalindrome(num,n))