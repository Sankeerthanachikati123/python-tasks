def first(firstname,lastname):
    print("hello " +  firstname  +     "my surname is"+ lastname )
first("sanku","chikati")

def my(cars):

  for i in cars:
    print(i)

cars=["merg","tesla","BMW"]
my(cars)

def  multi(*num):
    print("arbitary arguments" + num[2])
multi("test1","test2","test3")

def multiple(**num1):
    print("keywrod",num1["test3"])
multiple(test1="snaku",test2="sanku2",test3="sanku3")


def f1(*n):
    print(n)
f1(10,20,30,40,50)

s=lambda n:n*n
print(s(2))


def add(a,b):
    return(a+b)
print(add(4,5))


