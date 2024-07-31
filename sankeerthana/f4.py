str1=str(input("enter a string:"))
upper_case=0
lower_case=0
for i in str1:
    if  i.isupper():
        upper_case+=1
    else:
        lower_case+=1
print("UPPERCASE",upper_case,end=" ")
print("LOWERCASE",lower_case)
