#!/usr/bin/env python3
class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class LList(object):
    def __init__(self,head=None):
        self.head=head
class stack(object):
    def __init__(self):
        self.obj=LList()
    def push(self,node):
        if self.obj.head==None:
            self.obj.head=node
        else:
            temp2=self.obj.head
            temp2.next=node
            self.obj.head=node

    def printl(self):
        A=[]
        temp=self.obj.head
        if temp:
            while temp:
                A.append(temp.value)
                temp=temp.next
        print(A)
            
       
    #def pop(self):
    #    temp=self.obj.head
    #    if temp!=None:
    #        while temp.next:
    #            temp=temp.next
    #        deleted_element=temp.next
if __name__=='__main__':
    node=Node(1)
    obj2=stack()
    obj2.push(node)
    node2=Node(2)
    obj2.push(node2)
    node3=Node(3)
    obj2.push(node3)
    obj2.printl()
    



