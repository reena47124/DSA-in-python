#stack
#top element of the stack
class Stack:
    def __init__(self,capacity):
        self.a=[0]*capacity
        self.capacity=capacity
        self.top=-1
    def push(self,x):
        if self.top==self.capacity-1:
            print("stack overflow")
            return
        self.top+=1
        self.a[self.top]=x
    def peek(self):
        if self.top==-1:
            print("stack is empty")
            return -1
        value=self.a[self.top]
        return value
s=Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.a)
print("the top element is:",s.peek())        