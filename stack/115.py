#stack
#pop a value out of the stack
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
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        value=self.a[self.top]
        self.top-=1
        return value
s=Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.a)
print(s.pop())            


