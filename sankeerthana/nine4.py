'''
    list1=[1,2,3,4,]
new_num=list1

new_num[0]=9
print(new_num)
print(id(new_num))*\
copy.copy-shallowcopy
copy.deepcopy-deepcopy
'''
import copy
old=[[1,2,3],[4,5,6],[7,8,9]]
new=copy.deepcopy(old)
new[0][2]='b'
print(old)
print(new)
