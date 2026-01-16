class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None


def buildTree(preorder, inorder):

    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = Node(root_val)

    mid = inorder.index(root_val)

    root.left = buildTree(preorder[1:mid+1],inorder[:mid])

    root.right = buildTree(preorder[mid+1:],inorder[mid+1:])

    return root



from collections import deque
def buildTree_v2(preorder, inorder):

    if not preorder or not inorder:
        return None
    
    p = deque(preorder)
    n = len(preorder)

    lookup = {val:i for i,val in enumerate(inorder) }

    def rec(start,end):

        if start > end:
            return None
        
        root_val = p.popleft()
        root = Node(root_val)

        mid = lookup[root_val]

        root.left = rec(start,mid-1)

        root.right = rec(mid+1,end)

        return root
    
    return rec(0,n-1)


def printPreorder(root):
    if not root:
        return
    print(root.data, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)

def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)
    

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


root1 = buildTree(preorder, inorder)
root2 = buildTree_v2(preorder, inorder)

print("Tree1 Inorder:")
printInorder(root1)
print("\nTree1 Preorder:")
printPreorder(root1)
