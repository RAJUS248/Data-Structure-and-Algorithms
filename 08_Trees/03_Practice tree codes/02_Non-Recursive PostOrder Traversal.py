class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):

    if not root:
        return []

    stack = [root]
    res = []

    while stack:

        node = stack.pop()
        res.append(node.data)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return res[::-1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(postorder(root))