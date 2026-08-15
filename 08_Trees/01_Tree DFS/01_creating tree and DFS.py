class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if node:
        # root
        print(node.data, end =" ")

        # left
        pre_order(node.left)

        #right
        pre_order(node.right)

def in_order(node):
    if node:

        # left
        in_order(node.left)

        # root
        print(node.data, end =" ")

        #right
        in_order(node.right)

def post_order(node):
    if node:

        # left
        post_order(node.left)

        #right
        post_order(node.right)

        # root
        print(node.data, end =" ")
    

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)
root.right.left = TreeNode(40)
root.right.right = TreeNode(60)


print("\n" + "="*30)
print("Pre-order Traversal :")
pre_order(root)
# Output: 10 5 2 7 15
print("\n" + "="*30)

print("\n" + "="*30)
print("in-order Traversal :")
in_order(root)
# Output: 10 5 2 7 15
print("\n" + "="*30)

print("\n" + "="*30)
print("post-order Traversal :")
post_order(root)
# Output: 10 5 2 7 15
print("\n" + "="*30)