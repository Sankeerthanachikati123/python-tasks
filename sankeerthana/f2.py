def fun(a,b):
    for i in range(a,b+1):
        if (i%7==0 and i%5!=0):
             print(i,end=", ")

fun(2000,3200)