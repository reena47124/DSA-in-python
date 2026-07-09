#linked list
#deletion at the beginning of the linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def deletefirst(head):
    if head is None:
        return None
    temp=head
    head=head.next
    del temp
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
head.next.next=Node(3)
head.next.next.next=Node(4)
display(deletefirst(head))                   