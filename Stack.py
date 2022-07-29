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
        temp=self.obj.head
        if temp!=None:       
            while temp.next!=None:      
                temp=temp.next
            temp.next=node         
        else:
            self.obj.head=node
    def printl(self):
        A=[]
        temp=self.obj.head
        if temp:
            while temp:
                A.append(temp.value)
                print(temp.value)
                temp=temp.next
        print(A)
    def pop(self):
        temp=self.obj.head
        if temp!=None:
            if temp.next!=None:
                while temp.next!=None:
                    temp2=temp
                    temp=temp.next 
                temp2.next=None 
            else:
                self.obj.head=None
                print('hi')
        else:
            print('No element in this Linkedlist to pop')
if __name__=='__main__':
    node=Node(1)
    obj2=stack()
    obj2.push(node)
    node2=Node(2)
    obj2.push(node2)
    node3=Node(3)
    obj2.push(node3)
    
    node4=Node(4)
    obj2.push(node4)
    node5=Node(5)
    obj2.push(node5)
    node6=Node(6)
    obj2.push(node6)
    obj2.printl()
    obj2.pop()
    obj2.printl()
    obj2.pop()
    obj2.printl()
    obj2.pop()
    obj2.printl()
    obj2.pop()
    obj2.printl()
    obj2.pop()
    obj2.printl()
    obj2.pop()
    obj2.printl()
    obj2.pop()
    obj2.printl()
    node7=Node(7)
    obj2.push(node7)
    obj2.printl()




