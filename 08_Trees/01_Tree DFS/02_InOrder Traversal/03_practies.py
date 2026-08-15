class Treenode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(root):

    res = []

    def dfs(node):

        if not node:
            return
        
        res.append(node.data)
        dfs(node.left)
        dfs(node.right)
        
    dfs(root)
    return res

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
print(pre_order(root))