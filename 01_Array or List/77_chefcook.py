def chefcook(n,p,arr):

    arr.sort(key=lambda x:x[1])
    count =0
    for e,m in arr:

        if e >= p:
            count += 1
            p = max(p,m)
        
    return count

n = 3
p = 3
arr = [[3,7],[3,6],[6,8]]
print(chefcook(n,p,arr))