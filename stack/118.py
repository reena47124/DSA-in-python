#stack
#stack implementation using dynamic array i.e. list.
class Stack:
    def __init__(self):
        self.a=[]
    def push(self,x):
        self.a.append(x)
    def pop(self):
        if len(self.a)==0:
            print("stack is underflow")
            return -1
        value=self.a.pop() 
        return value
    def peek(self):
        if len(self.a)==0:
            print("stack is empty")
        value=self.a[-1]
        return value
    def isEmpty(self):
        if len(self.a)==0:
            return True
        return False
    def size(self):
        return len(self.a)
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("the stack is:",s.a)
print("removed element:",s.pop())
print("top element:",s.peek())
print("stack is empty:",s.isEmpty())
print("size of the stack:",s.size())


           