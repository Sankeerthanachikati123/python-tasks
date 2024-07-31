import csv
with open("C:\\Users\LENOVO\Downloads\\username.csv","r") as file:
     f1=csv.reader(file)
     for i in f1:
             print(i)