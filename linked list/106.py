#linked list
#traversal singly linked list,recursive approach.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traversal_list(head):
    if head is None:
        return
    print(head.data,end="")
    if head.next is not None:
        print("->",end="")
    traversal_list(head.next) 
head=Node(1)
head.next=Node(2)
head.next.next=Node(4)
head.next.next.next=Node(8)
traversal_list(head)               
