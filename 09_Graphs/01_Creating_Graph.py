# adjacency list implementation  for undirection graph

def create_graph(edges):
    graph = {}

    for u,v in edges:
        if u not in graph:
            graph[u] = []

        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    return graph



# adjacency list implementation  for direction graph

def create_graph_directional(edges):
    graph = {}

    for u,v in edges:
        if u not in graph:
            graph[u] = []

        if v not in graph:
            graph[v] = []

        graph[u].append(v)
    
    return graph



edges = [[0,1],[0,2],[1,3],[2,3]]
direct = create_graph_directional(edges)
undirect = create_graph(edges)


print("\nundirection graph")
for node in undirect:
    print(f"{node} --> {undirect[node]}")

print("direction graph")
for node in direct:
    print(f"{node} --> {direct[node]}")