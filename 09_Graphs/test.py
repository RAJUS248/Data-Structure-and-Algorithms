def directional_graph(edges):

    graph = {}

    for u,v in edges:

        if u not in graph:
            graph[u] = []

        graph[u].append(v)

    return graph
   

edges = [[1,3],[1,4],[2,3],[2,4],[4,3]]

direction = directional_graph(edges)

# print("undirection graph")
# for node in undirection:
#     print(f"{node} --> {undirection[node]}")

print("Direction Graph")
print(direction)

for node in direction:
    print(f"{node} --> {direction[node]}")


# def undirectional_weighted_graph(edges):

#     graph = {}

#     for u,v,w in edges:

#         if u not in graph:
#             graph[u] = []

#         if v not in graph:
#             graph[v] = []

#         graph[u].append((v,w))
#         graph[v].append((u,w))

#     return graph

# def directional_weighted_graph(edges):

#     graph = {}

#     for u,v,w in edges:

#         if u not in graph:
#             graph[u] = []

#         graph[u].append((v,w))
        

#     return graph

# edges = [
#     ('A', 'B', 4),
#     ('A', 'C', 2),
#     ('B', 'C', 5),
#     ('B', 'D', 10),
#     ('C', 'D', 3)
# ]

# w_undirectional = undirectional_weighted_graph(edges) 
# w_directional = directional_weighted_graph(edges) 

# print("undirectional_weighted_graph")

# for node in w_undirectional:
#     print(f"{node} --> {w_undirectional[node]}")


# print("directional_weighted_graph")

# for node in w_directional:
#     print(f"{node} --> {w_directional[node]}")
