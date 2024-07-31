class A:
    def display(self):
        print("class 1")
class B:
    def display(self):
        print("class b ")
class demo(B,A):
    def show(self):
        print("class demo method")

d=demo()
d.display()
print(demo.mro())