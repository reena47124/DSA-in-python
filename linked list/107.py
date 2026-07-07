#linked list
#insertion,at the front of linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_front(head,data):
    newNode=Node(data)
    newNode.next=head
    return newNode
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
#head=insert_front(head,0)
#print_list(head) 
print_list(insert_front(head,0))                  