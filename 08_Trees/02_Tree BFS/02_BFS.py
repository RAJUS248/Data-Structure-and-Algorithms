from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal(root_node):

    if not root_node:
        return
    
    queue = deque([root_node])

    print("Level-Order Output:")

    while queue:
        
        cur_node = queue.popleft()

        print(cur_node.data, end=" ")

        if cur_node.left:
            queue.append(cur_node.left)

        if cur_node.right:
            queue.append(cur_node.right)

    
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)
root.right.left = TreeNode(40)
root.right.right = TreeNode(60)


# --- Execution ---
print("\n" + "="*30)
level_order_traversal(root) 
# Output: 10 20 30 40 60 40 60 
print("\n" + "="*30)