class student :
    def __int__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def m1(self):
        print("hi")

    def m2(self):
        print("the name is ",self.name,"and roll is",self.rollno )
class teacher(student):
    def __init__(self,salary,role):
        self.salary=salary
        self.role=role
    def m3(self):
        print("the salary",self.salary,"the role is ",self.role)
s1=teacher("5000","developer")
s1.m1()
s1.m2()