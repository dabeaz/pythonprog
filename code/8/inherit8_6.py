class Parent(object):
    def spam(self):
        print('Parent.spam')

class A(Parent):
    def spam(self):
        print('A.spam')
        super().spam()

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(Parent):
    def spam(self):
        print('C.spam')
        super().spam()

class D(Parent):
    def spam(self):
        print('D.spam')
        super().spam()
