from collections import defaultdict
def creating_graph(edges):

    graph = defaultdict(list)

    for u,v in edges:

        graph[u].append(v)
        graph[v].append(u)

    print (dict(graph))
    return graph

def dfs(graph, node ,visited = None, lst = None):
    
    if visited is None:
        visited = set()
    
    if lst is None:
        lst = []

    visited.add(node)
    lst.append(node)

    for baju in graph[node]:
        if baju not in visited:
            dfs(graph,baju,visited,lst)

    return lst
    
def dfs_using_stack(graph,start):

    visited = {start}
    stack = [start]
    lst = []

    while stack:
        node = stack.pop()
        lst.append(node)

        for baju in graph[node]:
            if baju not in visited:
                visited.add(baju)
                stack.append(baju)

    print(lst)



edges = [[0,1],[0,2],[1,3],[2,3]] # [[0,1],[0,2],[3,5],[5,4],[4,3]]
graph = creating_graph(edges)

print(dfs(graph,0))
dfs_using_stack(graph,0)