class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    
          
   
class SLL:            
    def __init__(self):  
        self.head = None
  

    def insert_at_end(self,data):
        new_node = Node(data)
        # empty 
        if self.head is None:
            self.head = new_node
            return

        # 1 node
        if self.head.next is None:
            self.head.next = new_node
            return
    
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node
        return

    def dlt_nth_node(self,n):

        count = 0
        cur = self.head

        while cur:
            count += 1
            cur = cur.next

        rem = count - n

        if rem == 0:
            return self.head.next

        cur = self.head
        while rem > 1:
            cur = cur.next
            rem -= 1

        cur.next = cur.next.next
        return self.head


    def print_nodes(self):
        cur_node = self.head
        
        while cur_node is not None:
            print(cur_node.data, end = "->")
            cur_node = cur_node.next

        print("None")

sll = SLL()

sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)
sll.insert_at_end(50)

sll.print_nodes()

sll.dlt_nth_node(2)
sll.print_nodes()
