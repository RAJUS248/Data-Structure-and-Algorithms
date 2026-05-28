def removeKdigits(num, k):

    n = len(num)
    maxi = num[k-1:n]

    for i in range(n):  

        if i <= k:
            check = num[0:i+1] + num[k+i+1:n]  
  
            if int(check) < int(maxi):  
                maxi = check
    
        else:
            break  

    return maxi

num = "5337"
k = 2
print(removeKdigits(num,k))

def
