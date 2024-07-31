# def remove(input):
#         return " ".join (sorted(set(input),key=input.index))
 #input=str(input("enter any string"))
#print(remove(input))

def remove_duplicates(input1):
    return  (" ".join(set(input1)))
input1=str(input("enter a string:"))
print(remove_duplicates(input1))