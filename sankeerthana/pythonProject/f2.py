def sort_list(list1,list2):
    l1=[]
    i,j=0,0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            l1.append(list1[i])
            i=i+1
        else:
            l1.append(list2[j])
            j=j+1

    while i<len(list1):
        l1.append(list1[i])
        i=i+1
    while j<len(list2):
        l1.append(list2[j])
        j=j+1
    return l1
list1=[1,2,3,4]
list2=[5,9,2,4]
sort_list(list1,list2)