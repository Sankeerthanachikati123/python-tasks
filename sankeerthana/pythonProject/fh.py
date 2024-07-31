f=open("C:\\Users\LENOVO\PycharmProjects\pythonProject\calculator.py","r")
content=f.read()
f.close()
print(content)


with open("C:\\Users\LENOVO\PycharmProjects\pythonProject\list.py","r") as files:
  data=files.read()
print(data)

f1=open("C:\\Users\LENOVO\PycharmProjects\pythonProject\loops.py","w")
data2=f1.write("hi infinitude")
print(data2)
f1.close()


