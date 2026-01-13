# Queue and # Stack
from collections import deque
class TreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def leftsum_using_queue(root):

    if not root:
        return 0
    
    queue = deque([root])
    left_sum = 0

    while queue:

        node = queue.popleft()

        if node.left:
            if not node.left.left and not node.left.right:
                left_sum += node.left.data

            else:
                queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return left_sum

def leftsum_using_stack(root):

    if not root:
        return 0

    stack = [root]
    total = 0

    while stack:

        node = stack.pop()

        if node.left:

            if not node.left.left and not node.left.right:
                total += node.left.data

            else:
                stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return total

        


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
        
print(leftsum_using_queue(root))
print(leftsum_using_stack(root))
