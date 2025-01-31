import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Точка ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Пример
point1 = Point(0, 0)
point2 = Point(3, 4)

point1.show()  # Точка (0, 0)
point2.show()  # Точка (3, 4)

point1.move(1, 1)
point1.show()  # Точка (1, 1)

print("Расстояние между точками:", point1.dist(point2)) 

'''
В классе Point мы задаем координаты точки и реализуем методы:
show, который выводит координаты.
move, который изменяет координаты точки на величины dx и dy.
dist, который вычисляет расстояние между текущей точкой и другой точкой с помощью формулы для расстояния между двумя точками.

'''