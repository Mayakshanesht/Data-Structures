#!/usr/bin/env python3
# syntax=[]
class List(object):
    def __init__(self,B):
        self.B=B
    def print(self,B):
        print(self.B)
    def operations(self,operation,value):
        if operation=='append':
            self.B.append(value)
        elif operation=='extend':
            self.B.extend(value)
        elif operation=='sort':
            self.B.sort()
        elif operation=='reverse':
            self.B.reverse()
        elif operation=='copy':
            self.C=self.B.copy()
        elif operation=='insert':
            self.B.insert(-1,value)
        elif operation=='sorted':
            self.D=sorted(self.B)
            print(self.D)
        else:
            self.B.pop()
if __name__=='__main__':
    try:
        B=[1,2,4,5,4,6]
        #D='Mayur'
        obj=List(B)
        E=obj.operations('append',10000)
        obj.print(E)
    except SyntaxError:
        pass

        

