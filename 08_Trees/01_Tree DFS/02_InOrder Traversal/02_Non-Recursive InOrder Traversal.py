class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):

    if not root: 
        return []

    stack = []
    res = []
    cur = root

    while stack or cur:
         
        while cur:

            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        res.append(cur.data)

        cur = cur.right

    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
print(inorder(root))