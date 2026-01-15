from collections import deque

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal_or_bfs(root):

    queue = deque([root])
    res = []

    while queue:

        node = queue.popleft()
        res.append(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return res
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)   

print(level_order_traversal_or_bfs(root))