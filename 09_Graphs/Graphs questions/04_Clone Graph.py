from collections import deque

# Node class
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):

        if node is None:
            return None

        # Original Node -> Cloned Node
        clones = {}

        # Clone the first node
        clones[node] = Node(node.val)

        queue = deque([node])

        while queue:

            current = queue.popleft()

            for neighbor in current.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[current].neighbors.append(clones[neighbor])

        return clones[node]


# --------------------------
# Create the graph manually
# --------------------------

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect nodes
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


# Clone the graph
solution = Solution()
clone = solution.cloneGraph(node1)

print("Original Node:", node1.val)
print("Cloned Node:", clone.val)