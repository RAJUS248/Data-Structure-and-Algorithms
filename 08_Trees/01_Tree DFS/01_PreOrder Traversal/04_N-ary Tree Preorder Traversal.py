class Node:

    def __init__(self,data,children=None):

        self.data = data
        self.children = children if children else []

def preorder(root):

    if not root:
        return []
    
    stack = [root]
    res = []

    while stack:

        node = stack.pop()
        res.append(node.data)

        for child in reversed(node.children):
            stack.append(child)

    return res

def preorder_recurcive(root):

    resr = []
    
    def dfs(node):
        if not node:
            return

        resr.append(node.data)

        for child in node.children:
            dfs(child)

    dfs(root)
    return resr

root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

print(preorder(root))
print(preorder_recurcive(root))