def vowelStrings(words, queries):

    seen = {"a","e","i","o","u"}
    vowels = [] 

    for word in words:

        n = len(word)

        s = 0
        e = n-1

        if word[s] in seen and word[e] in seen:
            vowels.append(1)

        else:
            vowels.append(0)

    prefix_sum = []
    cur_sum = 0
    for num in vowels:

        cur_sum += num

        prefix_sum.append(cur_sum)


    res = []
    for i in range(len(queries)):
        l = queries[i][0]
        r = queries[i][1]

        if l == 0:
            rem = prefix_sum[r] - 0
    
        else:
            rem = prefix_sum[r] - prefix_sum[l-1]
        res.append(rem)

    return res


words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

print(vowelStrings(words,queries))