class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def solve(self):
        # 1. READ INPUT
        # Assuming input comes from standard input as a string like "2 1 N 1"
        # We strip spaces and split. If it's a raw string '21N1', we list(s).
        s = input().split() # Example Input: 2 1 N 1
        
        if not s or s[0] == 'N':
            return

        # 2. BUILD THE TREE (Level Order Insertion)
        root = Node(s[0])
        queue = [root]
        i = 1
        
        while i < len(s) and queue:
            current_node = queue.pop(0)
            
            # Add Left Child
            if i < len(s) and s[i] != 'N':
                current_node.left = Node(s[i])
                queue.append(current_node.left)
            i += 1
            
            # Add Right Child
            if i < len(s) and s[i] != 'N':
                current_node.right = Node(s[i])
                queue.append(current_node.right)
            i += 1

        # 3. PRINT POST-ORDER (The Actual Logic)
        self.postOrder(root)

    def postOrder(self, node):
        if node is None:
            return
        
        # Go Left
        self.postOrder(node.left)
        # Go Right
        self.postOrder(node.right)
        # Print Root
        print(node.data)

# --- Driver Code ---
sol = Solution()
# If you run this, type: 2 1 N 1
sol.solve()