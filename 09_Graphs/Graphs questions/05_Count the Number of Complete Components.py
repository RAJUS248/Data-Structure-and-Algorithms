from collections import deque
def bfs(graph, start):

    visited = {start}
    lst = []
    queue = deque([start])

    while queue:

        node = queue.popleft()
        lst.append(node)

        for nibr in graph[node]:

            if nibr not in visited:
                visited.add(nibr)
                queue.append(nibr)

    return lst

def countCompleteComponents(n, edges):

    graph = {i:[] for i in range(n)}

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    components = []
    seen = set()

    ans = 0
    for i in range(n):

        if i not in seen:
            component = bfs(graph,i)
            components.append(component)
            seen.update(component)

            actual_edge = 0

            for node in component:

                actual_edge += len(graph[node])
            
            actual_edge //=2 

            k = len(component)

            expected_edges = k * (k - 1) // 2

            if actual_edge == expected_edges:
                ans += 1

    return ans

    
n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
graph = countCompleteComponents(n,edges) 
print(graph)



