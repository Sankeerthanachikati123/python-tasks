#1
f1=open("C:\\Users\LENOVO\PycharmProjects\pythonProject\input.tx","r")
data=f1.read()
f1.close()
print(data)
#2
str=input("enter the data:")
f2=open("C:\\Users\LENOVO\PycharmProjects\pythonProject\loops.py","w")
data3=f2.write(str)
f2.close()
print(data3)
#3
def copy(source,destination):
    try:
        with open(source,'r') as src_file:
            data1=src_file.read()
        with open(destination,"w") as dest_file:
            dest_file.write(data1)
        print(f"contents copied from {source} to {destination} successfully")
    except FileNotFoundError   as e:
        print(f"error:{e}")

copy("input.tx","input2.txt")
#4
import pandas as p
def display(file_name):
    try:
        data=p.read_csv(filename)
        print(data.to_string(index=false))
    except FileNotFoundError :
        print("file not found")
    except Exception as e:
        print("unexepected error")

display("")
#5
