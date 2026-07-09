#linked list
#deletion at the end of the linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def delete_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    secondlast=head  #initialisation
    while secondlast.next.next is not None:
        secondlast=secondlast.next  
    secondlast.next=None
    return head
def display(head):
    temp=head
    while temp is not None:
        print(temp.data,end="")
        if temp.next is not None:
            print("->",end="")
        temp=temp.next 
    print()
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
display(delete_end(head))                       