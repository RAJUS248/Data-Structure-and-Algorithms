
# postorder  left -> right -> root
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):

    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
postorder(root)




# postorder  left -> right -> root
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder_v2(root):

    result = []

    def recursive(root, result):
        if not root:
            return
        recursive(root.left, result)
        recursive(root.right, result)
        result.append(root.data)

    recursive(root, result)
    print()
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(postorder_v2(root))