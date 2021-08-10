import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x)
        print(self.y)


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def show(self):
        super().show()
        print(self.radius)


class Rect(Point):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def show(self):
        super().show()
        print(self.width)
        print(self.length)


r = Rect(10, 10, 20, 30)
r.show()


