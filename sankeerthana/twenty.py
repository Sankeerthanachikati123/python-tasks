class MyIterator:
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
my_iter=MyIterator([1,2,3,4,5,6])
for i in my_iter:
    print(i)
print ()