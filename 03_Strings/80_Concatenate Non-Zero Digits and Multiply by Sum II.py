def sumAndMultiply(s, queries):
    
    n = len(s) 
    mod = 10 ** 9 + 7
    digitsum = [0] * n
    non_zero_count = []
    numberupto = [0] * n
    c = 1
    for i in range(n):

        num = int(s[i])


        if num != 0:

            numberupto[i] = (numberupto[i-1]*10 + num)
            digitsum[i] = (num + digitsum[i-1])
            non_zero_count.append(c)
            c += 1
            

        else:
            numberupto[i] = (numberupto[i-1])
            digitsum[i] = (digitsum[i-1])
            non_zero_count.append(c-1)
            
    res = []

    for lst in queries:

        start = lst[0]
        end = lst[1]

        sums = 0
        k = 0

        x = 0

        if start == 0:
            sums = digitsum[end]
            k = non_zero_count[end]

            x = numberupto[end]

        else:
            sums = digitsum[end] - digitsum[start-1]

            # find k
            k = non_zero_count[end] - non_zero_count[start-1]

            x = numberupto[end] - (numberupto[start-1] * 10**k)

        res.append((x * sums) % mod)

    return res

        

         

        



        

            
        


s = "10203004"
queries = [[0,7],[1,3],[4,6]]

print(sumAndMultiply(s,queries))