def read(file):
    try:
        with open("filename","r")as f:
            s1=f.readlines()
            for i in reversed(s1):
                print(line.rstrip())
    except FileNotFoundError:
        print("error")
file=input("enter the filename")
read(file)