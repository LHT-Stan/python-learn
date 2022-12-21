class Color:
    def __init__(self, r=0, g=0, b=0):
        self._red = r
        self._green = g
        self._blue = b

    @property
    def r(self):
        return self._red

    @property
    def g(self):
        return self._green

    @property
    def b(self):
        return self._blue

    def luminance(self):
        return 0.299 * self._red + 0.587 * self._green + 0.114 * self._blue

    def toGray(self):
        gray = round(self.luminance(), 0)
        return Color(gray, gray, gray)

    # 亮度差小于128
    def isCompatible(self, other):
        return abs(self.luminance() - other.luminance()) >= 128

    def __str__(self):
        return f"({self._red}, {self._green}, {self._blue})"


if __name__ == '__main__':
    c = Color(255, 0, 0)
    yellow = Color(255, 255, 0)
    print(c.r)
    print(yellow.luminance())
    print(yellow.toGray())
    print(yellow)
    print(c.isCompatible(yellow))
