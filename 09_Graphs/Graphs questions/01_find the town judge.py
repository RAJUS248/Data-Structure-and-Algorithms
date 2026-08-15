# from collections import defaultdict
def findJudge(n,trust):
    incomming = {i:0 for i in range(1,n+1)}
    outgoing = {i:0 for i in range(1,n+1)}

    for src,dest in trust:

        incomming[dest] += 1
        outgoing[src] += 1

    for i in range(1,n+1):
        if outgoing[i] == 0 and incomming[i] == n-1:
            return i
    
    return -1
n = 3
trust = [[1,3],[2,3]]
print(findJudge(n,trust))