def compress(chars):
    
    w = 0
    r = 0

    while r < len(chars):

        ch = chars[r]
        count = 0

        while r < len(chars) and chars[r] == ch:
            r += 1
            count += 1

        chars[w] = ch
        w += 1

        if count > 1:
            for c in str(count):
                chars[w] = c
                w += 1

    return w

chars = ["a","b","b","b","c","c","c","c"]
print(compress(chars))

# or

def compress_v2(chars):
    
    n = len(chars)
    w = 0
    count = 1

    for i in range(1,n+1):
        
        if i < n and chars[i] == chars[i-1]:
            count += 1

        else:
            chars[w] = chars[i-1]
            w += 1


            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1
            
            count = 1

    return w,chars

chars = ["a","b","b","b","c","c","c","c"]
print(compress_v2(chars))