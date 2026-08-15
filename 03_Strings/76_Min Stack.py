class MinStack(object):

    w = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    c = [[],[-2],[0],[-3],[],[],[],[]]  

    w[0] = c[0]

    for i in range(1,len(w)):

        fun = w[0]
        fun(c[i])


    def __init__(self,res,op):
        self.res = []
        self.op = []

    
    def push(self,value):
        self.res.append(value)
        self.op.append("Null")
        

    def pop(self):
        self.res.pop()
        self.op.append("Null")
        

    def top(self):
        self.op.append(self.res.pop())
        
    def getMin(self):
        self.op.append(self.res.pop(min(self.res)))
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()