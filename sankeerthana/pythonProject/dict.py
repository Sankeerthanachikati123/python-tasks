d={}
print(type(d))
d[1]='a'
d[2]='b'
d[3]='c'
d[4]='d'
d[5]='e'
d[6]='f'
print(d)
del d[3]
print(d)
len(d)
d.pop(2)
print(d)
d.popitem()
print(d)

d1=d.copy()
print(d1)