
word=str(input("enter a word"))
sum=0
with open ("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\practice.py","r") as f:
    for i in f:
        words=i.split()
        for j in words:
            if(i==word):
                sum=sum+1
    print(sum)
