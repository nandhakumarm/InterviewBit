class MinStack(object):

    def __init__(self):
        self.min_index=-1
        self.stack=[]
        

    def push(self, x):
        self.stack.append(x)
        if self.min_index==-1:
            self.min_index=0
        elif self.stack[self.min_index]>x:
            self.min_index=len(self.stack)-1
        
        

    def pop(self):
        temp=len(self.stack)-1
        if len(self.stack)!=0:
            self.stack.pop()
        if temp==self.min_index:
            self.min_index=0
            for i in range(1,len(self.stack)):
                if self.stack[self.min_index]>self.stack[i]:
                    self.min_index=i
                
    def top(self):
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return -1

    def getMin(self):
        if len(self.stack)!=0:
            return self.stack[self.min_index]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(1)
print obj.getMin()
obj.pop()
print obj.getMin()
print obj.top()
#param_4 = obj.getMin()