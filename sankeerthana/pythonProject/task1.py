#1
d={}
d[1]=501
d[2]=503
d[3]=504
d[4]=505
d[5]=506
print(d)


#a
print(d.keys())
print(d.values())

for i in d:
      print(i)


for i in d:
     print(d[i])

#b
print(d.pop(2))
print(d)


print(d)
#c
d["car"]="tesla"
print(d)
#d
s3=list(d)
print(type(s3))

print(s3)

#2
list1=[1,2,"sanku",3,4,5,"nice",6,7,8,9,"wow"]
#a
print(list1[:8])

#b
print(list1[8])
#c
list2=[111,2,37,4,90,6,77,8,9]
list2.sort()
print(list2)
list2.reverse()
print(list2)

#c

str2=input("enter a string")
s=("  ")
for i in str2:
        s=i+s
print(s)

#d
for i in range(1,100):

    if(i%5==0):
         print("the number is divisible by 5",i)
    else:
        print("the number is divisible by other than y")
print(i)

x=y=z="rani"
print(x)
print(y)
print(z)