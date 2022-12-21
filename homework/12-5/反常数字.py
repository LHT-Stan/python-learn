class AbnormalNum:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x

    def __floordiv__(self, other):
        return self.x // other.x

    def __mod__(self, other):
        return self.x % other.x

