# Inheritance 
class A:
    def show1(self):
        print("Class A")

class B(A):
    def show2(self):
        print("Class B")
        
class C(A):
    def show3(self):
        print("Class C")
class D(B,C):
    def show4(self):
        print("Class D")

obj = D()
obj.show1()
obj.show2()
obj.show3()
obj.show4()
