#!/usr/bin/env python3
class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue(object):
    def __init__(self,head=None, Last=None):
        self.head=head
        self.last=Last
class QueueOps(object):
    def __init__(self):
        self.obj=Queue()
    def enqueue(self,node):
        temp=self.obj.head
        if self.obj.last!=None:
            self.obj.last.next=node
            self.obj.last=self.obj.last.next
        else:
            self.obj.head=node
            self.obj.last=self.obj.head
    def dequeue(self):
        if self.obj.head!=None:
            temp=self.obj.head.next
            self.obj.head=temp

        else:
            print("No nodes in this queue")
    def peek(self):
        if self.obj.head!=None:
            print(self.obj.head.value)
        else:
            print('No element')
    def printqueue(self):
        temp=self.obj.head
        A=[]
        if temp:
            while temp!=None:
                print(temp.value)
                A.append(temp.value)
                temp=temp.next

if __name__=='__main__':
    ops=QueueOps()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    ops.enqueue(node1)
    ops.enqueue(node2)
    ops.enqueue(node3)
    ops.printqueue()
    ops.dequeue()
    ops.printqueue()
    ops.peek()
    




    