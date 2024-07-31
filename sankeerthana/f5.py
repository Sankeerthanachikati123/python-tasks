def fun(string1,string2):

      if len(string1)>len(string2):
          print("the maximum length  of string is ",len(string1))
      elif len(string1)<len(string2):
          print("the maximum length of string is",len(string2))
      elif len(string1)==len(string2):
          print(string1)
          print(string2)

string1=str(input("enter a string:"))
string2=str(input("enter another string:"))
fun(string1,string2)

