def unvisitedLeaves(N, leaves, frogs):
    
    visited = set()
    for i in range(N):

        pos = frogs[i]
        while pos <= leaves:

            if pos not in visited:
                visited.add(pos)

            pos += frogs[i]


    return leaves - len(visited)
            

N = 3
leaves = 4
frogs = [1,3,4,7]

print(unvisitedLeaves(N, leaves, frogs))


# optimize

def unvisitedLeaves_v2(N, leaves, frogs):
    
    visited = [False] * (leaves+1)
    
    frogs = set(frogs)

    for frog in frogs:

        if frog == 0 or frog > leaves:
            continue

        # if frog == 1:
        #     return 0

        if visited[frog] == True:
            continue

        for pos in range(frog,leaves+1,frog):

            visited[pos] = True


    count = 0

    for i in range(1,leaves+1):
        if visited[i] == False:
            count += 1

    return count


            

N = 3
leaves = 4
frogs = [1,3,4,7]

print(unvisitedLeaves_v2(N, leaves, frogs))