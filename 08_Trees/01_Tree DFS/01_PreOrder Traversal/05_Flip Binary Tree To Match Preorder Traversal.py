class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root,voyage):

    stack = [root]
    i = 0
    res = []

    while stack:

        node = stack.pop()
        res.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

voyage = [1,3,2]

print(preorder(root))
    