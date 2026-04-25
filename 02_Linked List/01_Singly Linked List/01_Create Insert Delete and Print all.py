class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
 
    
class SLL:   
  
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)

        # is empty
        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node

    def insert_at_position(self,data,pos):

        new_node = Node(data)

        if pos < 1:
            print("invalid position")
            return 

        if pos == 1:
            new_node.next = self.head 
            self.head = new_node
            return

        
        cur_pos = 1
        cur_node = self.head

        while cur_node and cur_pos < pos-1:
            cur_node = cur_node.next
            cur_pos += 1

        if cur_node is None:
            print("position is out of linked list length")
            return
        
        new_node.next = cur_node.next
        cur_node.next = new_node
            

    def delete_at_beginning(self):

        if self.head is None:
            print("list is empty")
            return 
        
        self.head = self.head.next
        return
    
    def delete_at_end(self):

        if self.head is None:
            print("list is empty")
            return 
        
        if self.head.next is None:
            self.head = None
            return
        
        cur_node = self.head

        while cur_node.next.next:
            cur_node = cur_node.next

        cur_node.next = None

    def delete_at_posisition(self,pos):
        
        if pos < 1:
            print("invalid position")
            return 
        
        if self.head is None:
            print("list is empty")
            return
        
        if pos == 1:
            self.head = self.head.next
            return
        
        cur_node = self.head
        cur_pos = 1

        while cur_node and cur_pos < pos - 1:
            cur_node = cur_node.next
            cur_pos += 1

        if cur_node is None or cur_node.next is None:
            print("invalid position")
            return
        
        cur_node.next = cur_node.next.next


    def print_sll(self):

        cur_node = self.head
        while cur_node:
            print(cur_node.data,end='->')
            cur_node = cur_node.next
        
        print('None')


# Driver code

if __name__ == "__main__":
    
    sll = SLL()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(4)


    sll2 = SLL()
    sll2.insert_at_end(1)
    sll2.insert_at_end(3)
    sll2.insert_at_end(4)

    sll.print_sll()
    sll2.print_sll()

    # # sll.insert_at_begining(30)
    # # sll.insert_at_begining(20)
    # # sll.insert_at_begining(10)
    # sll.insert_at_end(10)
    # sll.insert_at_end(20)
    # sll.insert_at_begining(30)
    # sll.insert_at_position(40,2)
    # sll.print_sll()
    # # sll.delete_at_beginning()
    # # sll.delete_at_end()
    # sll.delete_at_posisition(3)
    # sll.print_sll()

        
    


    
