myset={}
l1=[20,30,40,50,50]
l2=set(l1)
print(l2)


l2.add(46)
print(l2)
l3={45,55,65,75}
l3.update(l2)
print(l3)
l3.pop()
print(l3)
l3.remove(45)
print(l3)
l3.discard(99)
print(l3)
s3=l3.copy()
print(s3)

l1={1,2}
l3={3,4}
print(l1.union(l3))
print(l1.intersection(l3))
print(l1.difference(l3))
print(l1^l3)











