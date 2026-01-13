# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def preorderTraversal(root):
    
    if not root:
        return []

    stack = [root]
    res = []

    while stack:

        node = stack.pop()

        res.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(preorderTraversal(root))