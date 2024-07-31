#def div(a,b):

 #   print(a/b)

#def smart(fun):
 #   def inner(a,b):
  #      if a<b:
   #         a,b=b,a
    #    return fun(a,b)
    #return inner
#div1=smart(div)
#div1(1,4)

class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def email(self):
        return '{} {}@email.com '.format(self.first, self.last)

    @property
    def fullname(self):
           return '{} {} '.format(self.first,self.last)


    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first = None
        self.last = None


emp1=employee('john','switc')
emp1.first='jim'
emp1.fullname='sanku laddu'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
