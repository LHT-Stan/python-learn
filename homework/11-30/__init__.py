class Cube:
    # 立方体
    name = "立方体"  # 类属性

    def __init__(self, side):
        self.side_length = side

    def set_side(self, new_side):  # 设置变长的实例方法
        self.side_length = new_side

    def get_area(self):  # 求面积的实例方法
        # 求面积
        return 6 * self.side_length ** 2

    def get_volume(self):  # 求体积的实例方法
        # 求体积
        return self.side_length ** 3


if __name__ == "__main__":
    cube = Cube(5)
    print(cube.get_area())
    cube.set_side(10)
    a = cube.get_area()
    print(a)


