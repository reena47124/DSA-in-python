#linked list
#insertion,at the end of the linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_end(head,data):
    newNode=Node(data)
    if head is None:
        return newNode
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.next=newNode
    return head
def print_list(head):
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
head.next.next.next.next=Node(5)
print_list(insert_end(head,6))                               