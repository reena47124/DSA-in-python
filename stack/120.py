#stack
#pop operation using linked list
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
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("popped item is:",s.pop())      