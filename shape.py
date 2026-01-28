class Shape():
    def __init__(self, width,height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def __init__(self,width,height):
        Shape.__init__(self,width,height)
       

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self,side):
        Shape.__init__(self,side, side)
       

    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(3,4)
print(rectangle.calculate_area())

square = Square(5)
print(square.calculate_area())