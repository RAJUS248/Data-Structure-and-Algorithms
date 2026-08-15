def validPath(n, edges, source, destination):

    if not edges:
        return True
    
    graph = {}

    for u,v in edges:

        if u not in graph:
            graph[u] = []

        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    
    stack = [source]  # queue = deque([source]) use from collections import deque
    visited = {source}

    while stack:

        node = stack.pop()   # node = queue.popleft()   # FIFO (BFS)

        if node == destination:
            return True
        
        for nieghbor in graph[node]:

            if nieghbor not in visited:
                visited.add(nieghbor)
                stack.append(nieghbor)

    return False

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

solution = validPath(n,edges,source,destination)
print(solution)
