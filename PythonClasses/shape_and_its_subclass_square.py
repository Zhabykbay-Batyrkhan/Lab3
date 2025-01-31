class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# Пример
shape = Shape()
square = Square(5)

print("Площадь Shape:", shape.area()) 
print("Площадь Square:", square.area())  

'''
В классе Shape метод area по умолчанию возвращает 0.
Класс Square наследует от Shape, и его метод area возвращает площадь квадрата, вычисленную как квадрат длины стороны.
'''