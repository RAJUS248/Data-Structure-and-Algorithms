def magic_bulbs(n,bulbs):

    reach_vals = []
    for num in bulbs:

        num_sum = 0
        temp = num
        while temp > 0:
            ld = temp % 10
            num_sum += ld
            temp = temp // 10 

        reach = num + num_sum

        reach_vals.append(reach)

    from bisect import bisect_left
    res = []
    for x in reach_vals:
        pos = bisect_left(res,x)

        if pos == len(res):
            res.append(x)

        else:
            res[pos] = x

    return len(res)
    
n = 5
bulbs = [38, 2, 10, 2, 25]
print(magic_bulbs(n,bulbs))