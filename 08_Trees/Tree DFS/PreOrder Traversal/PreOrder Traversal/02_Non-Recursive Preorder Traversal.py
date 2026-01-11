class TreeNode:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

def Non_Recursive_Preorder(root):
    
    if not root:
        return
    
    stack = []
    stack.append(root)

    while stack:

        node = stack.pop()
        
        print(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
        
Non_Recursive_Preorder(root)
    


        