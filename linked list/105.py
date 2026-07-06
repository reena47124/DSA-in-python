#linked list
#traversal singly linked list,iterative approach
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverse_list(head):
    while head is not None:
        print(head.data,end="")
        if head.next is not None:
            print("->",end="")
        head=head.next
    print()
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
traverse_list(head)                    