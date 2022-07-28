#!/usr/bin/env python3
# It is a container which is used to store the homegeneous or heteregeneous elements in contagious memory locations and it is immutable,  syntax is (.,.,.)
class Tuple(object):
    def __init__(self,A):
        self.A=A
    def print_tuple(self):
        print(self.A)
if __name__=='__main__':
    try:
        A=(1,2,3)
        obj=Tuple(A)
        obj.print_tuple()
    except SyntaxError:
        pass