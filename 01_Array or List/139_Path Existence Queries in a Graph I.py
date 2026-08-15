def pathExistenceQueries(n, nums, maxDiff, queries):

    comp = [0] * n

    for i in range(1,n):

        if nums[i] - nums[i-1] > maxDiff:
            comp[i] = comp[i-1] + 1

        else:
            comp[i] = comp[i-1]

    res = []
    for s,e in queries:

        res.append(comp[s] == comp[e])

    return res
    
    # res = []
    # for s,e in queries:

    #     dif_check = True
    #     for i in range(s,e):

    #         dif = abs(nums[i] - nums[i+1])

    #         if dif > maxDiff:

    #             res.append(False)
    #             dif_check = False
    #             break
        
    #     if dif_check:
    #         res.append(True)

    # return res

# n = 2
# nums = [1,3]
# maxDiff = 1
# queries = [[0,0],[0,1]]
n = 4
nums = [2,5,6,8]
maxDiff = 2
queries = [[0,1],[0,2],[1,3],[2,3]]

print(pathExistenceQueries(n,nums,maxDiff,queries))