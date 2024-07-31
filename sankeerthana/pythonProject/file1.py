a=1243
print(type(a))
y=20.04
print(type(y))
x=10+5j
print(type(x))
print(x.real)
print(x.imag)

abc=10,20,30
print(type(abc))
a=[10,20,30,40]
b=bytes(a)
print(type(b))
c=bytearray(a)
print(type(c))
print(type(a))
s={10,20,27}
print(type(s))
d=frozenset(s)
print(type(d))


d={}
d[1]=777
d[2]=888
print(d)
print(type(d))

print("hello" + "world" )

print("world")
print(a,d,sep=",")

a=10
b="abc"
print("my name is %s" %(b))

name="sanku"
age=20
format1="my name is {} and i am {} years old " .format(name,age)
print(format1)


format2=f"my name is {name} and I am {age } years old "
print(format2)

print("my name is %s and my age is %d" %(b,age))

x=int(input("enter a number "))
y=int(input("enter a number "))
z=1/2*x*y
print(z)

x=int(input("enter a number "))
b=(x*(x+1)/2)
print(b)


sa=int(input("enter a number "))
if (sa%2==0):
       print("this is even ")

n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
if (n1>n2) :
      print("the largest is ",n1)
elif (n2>n3):
       print("the larger is ",n2)
else :
     print("the larger is ",n3)









