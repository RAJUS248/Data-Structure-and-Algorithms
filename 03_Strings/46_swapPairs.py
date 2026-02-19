def swapPairs(arr):

    res = []
    for s in arr:
        list_s = list(s)

        for i in range(0,len(s),2):
            if i + 1 < len(list_s):
                list_s[i],list_s[i+1] = list_s[i+1],list_s[i]

        res.append("".join(list_s))
    
    return res

arr = ['abcdefgh','pYth0nGo','PASSWORD']
print(swapPairs(arr))