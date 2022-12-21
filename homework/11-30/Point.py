import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(2,2)
    print(point2.distance(point1))
EEE