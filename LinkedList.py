class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist(object):
    def __init__(self,head=None):
        self.head=head
    def printlist(self):
        temp=self.head
        A=[]
        if temp:
            while temp:
                print(temp.value)
                A.append(temp.value)
                temp=temp.next
        print(A)
if __name__=='__main__':
    Llist=Linkedlist()
    Llist.head=Node(1)
    second=Node(2)
    third=Node(4)
    four=Node(10)
    Llist.head.next=third;
    second.next=four;
    third.next=second;
    Llist.printlist()