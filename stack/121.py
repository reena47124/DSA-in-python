#stack
#peek,isEmpty,size operations on stack using linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.count=0
    def push(self,data):
        temp=Node(data)
        temp.next=self.top
        self.top=temp
        self.count+=1
        print("pushed:",data)
    def pop(self):
        if self.top is None:
            print("stack is underflow")
            return -1
        temp=self.top
        self.top=self.top.next
        value=temp.data
        self.count-=1
        return value 
    def peek(self):
        if self.top is None:
            print("stack is empty")
            return -1
        value=self.top.data
        return value
    def isEmpty(self):
        return self.top is None
    def size(self):
        return self.count       
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("popped item is:",s.pop())
print("top item is:",s.peek())
print("stack is empty:",s.isEmpty())
print("size of the stack:",s.size()) 