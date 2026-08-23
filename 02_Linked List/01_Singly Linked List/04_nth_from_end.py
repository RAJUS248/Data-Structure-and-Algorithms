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
        
        # 2 or more nodes
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        return
    
    def nth_from_start(self,n):
      
        cur = self.head
        counts = 1

        while cur is not None:
            if counts == n:
                print(cur.data)
                return
            cur = cur.next
            counts += 1
       
        print(f"list as less then {n} nodes")


    def nth_from_start_v2(self,n):

        first = self.head
        
        if first is None:
            print("list is empty")
            return

        for _ in range(n - 1):
            
            first = first.next

            # final check after loop
            if first is None:
                print("n is larger than the list length")
                return

        print(first.data)
            

    def nth_from_end(self,n):
        total_len = 0
        cur = self.head

        while cur:
            total_len +=1
            cur = cur.next
        print(total_len)


        if n > total_len:
            print("invalid position")
            return None


        cur = self.head
        for _ in range(total_len - n):
            cur = cur.next
        
        print(cur.data)
        return
    
    def nth_from_end_v2(self,n):
        first = self.head
        second = self.head

        if first is None:
            print("list is empty")
            return
        
        for _ in range(n):
            if first is None:   # <-- check before moving
                print(f"{n} is out of range")
                return

            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        print(second.data)
    

    def print_list(self):

        curr = self.head

        while curr:
            print(curr.data, end = "->")
            curr = curr.next

        print("None")
        
sll = SLL()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)

sll.print_list()
sll.nth_from_start(3)
sll.nth_from_end(1)
sll.nth_from_start_v2(5)
sll.nth_from_end_v2(5)



