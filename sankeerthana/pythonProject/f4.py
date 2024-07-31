def flat(list):
    l1=[]
    for i in list:
        if isinstance(i,list):
             l1.extend(flat(i))

        else:

            l1.append(i)

    return flat(list)
list=[1,2,[3,7],4,7]
l1=flat(list)
print(flat(list))