# inorder  left -> root -> right

class Node:

    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None


def inorder(root):

    if not root:
        return

    inorder(root.left)
    print(root.data,end = " ")
    inorder(root.right)

def inorder_v2(root):

    if not root:
        return
    
    res = []

    while root:
        inorder_v2(root.left)
        res.append(root.data)
        inorder_v2(root.right)

    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)
print(inorder_v2(root))
