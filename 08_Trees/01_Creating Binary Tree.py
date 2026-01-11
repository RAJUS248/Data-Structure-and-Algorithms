class TreeNode:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def print_trees(node):

    if node:
    
        print(node.data)
        print_trees(node.left)
        print_trees(node.right)


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

print_trees(root)