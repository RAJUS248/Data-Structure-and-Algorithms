from collections import defaultdict

def create_weighted_graph_undirectional(edges):
    graph = defaultdict(list)

    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))

    return graph


def create_weighted_graph_directional(edges):
    graph = defaultdict(list)

    for u,v,w in edges:
        graph[u].append((v,w))
        

    return graph


edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'D', 3)
]

undirectional = create_weighted_graph_undirectional(edges)
directional = create_weighted_graph_directional(edges)


print("undirectional weighted graph")
for node in undirectional:
    print(f"{node} --> {undirectional[node]}")


print("\ndirectional weighted graph")
for node in directional:
    print(f"{node} --> {directional[node]}")