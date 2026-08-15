def minimumPushes(word):
        
    if len(word) <= 8:
        return len(word)

    res = 8
    k = 2
    ln = 8
    for i in range(9,len(word)+1):
        
        if i-ln <= 8:
            res += k

        else:
            k += 1
            res += k
            ln *= k
            
    
    return res

# word = "amrvxnhsewkoipjyuclgtdbfq"
# print(minimumPushes(word))

print(28%8)
print(28//8)
word = "amrvxnhsewkoipjyuclgtdbfq"

count = len(word) // 8
rem = len(word) % 8

res = 0
for i in range(1,count+1):

    res += 8 * i

res += (count + 1) * rem

print(res)
