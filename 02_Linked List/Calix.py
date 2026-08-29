class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
  

class SLL:  
  
    def __init__(self,head):
        self.head = None

    def detect_cycle(self,head):

        cur_node = self.head

        seen = set()

        while cur_node.next is not None and cur_node.data not in seen:

            seen.add(cur_node.data)
            cur_node = cur_node.next

        if cur_node.next is None:
            return False
        
        else:
            return True
        
sll = Node(1)
sll1.Node(1)
sll.Node(1)
sll.Node(1)
sll.Node(1)
sll.detect_cycle()
