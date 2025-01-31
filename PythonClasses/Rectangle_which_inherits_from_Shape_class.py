class Shape:
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Пример
rectangle = Rectangle(5, 3)
print("Площадь Rectangle:", rectangle.area())  # 15