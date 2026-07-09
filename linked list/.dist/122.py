#linked list
#insert a node at a specific position in a linked list,using iterative approach
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_pos(head,pos,val):
    if pos<1:
        return head
    if pos==1:
        newNode=Node(val)
        newNode.next=head
        return newNode
    current=head
    for i in range(1,pos-1):
        if current is None:
            return head
        current=current.next
    if current is None:
        return head
    newNode=Node(val)
    newNode.next=current.next
    current.next=newNode
    return head
def display(head):
    current=head
    while current is not None:
        print(current.data,end="")
        if current.next is not None:
            print("->",end="")
        current=current.next
    print()
head=Node(1)
head.next=Node(2)
head.next.next=Node(4) 
pos,val=3,3 
display(insert_pos(head,pos,val))              
            