class shape:
    pi=3.14
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
     def __init(self,radius):
         self.radius=radius
     def area(self):
         return pi*(self.radius**2)
     def perimeter(self):
        return 2*pi * self.radius


class rectangle(shape):
    def __init__(self, length,radius):
        self.length = length
        self.radius=radius

    def area(self):
        return self.length*self.radius

    def perimeter(self):
        return 2 * (self.length+self.radius)
shape1=rectangle(20,30)
print(shape1.area())