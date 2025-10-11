if __name__ == '__main__':
    N = int(input())

    lst = []
    
    for _ in range (N):
        
        cmd_lst = input().strip().split()
        cmd = cmd_lst[0]
        
        if cmd == "insert":
            i = int(cmd_lst[1])
            e = int(cmd_lst[2])
            lst.insert(i,e)
            
        elif cmd == "print":
            print(lst)
            
        elif cmd == "remove":
            e = int(cmd_lst[1])
            lst.remove(e)
            
        elif cmd == "append":
            e = int(cmd_lst[1])
            lst.append(e)
            
        elif cmd == "sort":
            lst.sort()
            
        elif cmd == "pop":
            lst.pop()
            
        elif cmd == "reverse":
            lst.reverse()
            

# inputs
"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""



