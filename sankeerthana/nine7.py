class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
          return vector(self.x+other.x,self.y+other.y)


v1=vector(12,13)
v2=vector(11,13)
v3=v1+v2
print(v3.x)
print(v3.y)
