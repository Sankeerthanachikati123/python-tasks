class Fileutility:
 def read(self,file):
    try:
        with open(file,"r") as files:
             return files.read()
    except FileNotFoundError:
         return None
 def copy(self,file1,file2):
     try:
       with open(file1,"r") as f1:

           data=f1.read()
       with open(file2,"w") as f2:
         f2.write(data)
     except FileNotFoundError:
          return none
 def write(self,file3,content):
     try:
         with open(file3,"w") as f3:
                f3.write(content)
     except RecursionError:
         print("none")

f7=Fileutility()
f7.write("length.py","wow")