# 三角形面积
from math import sqrt

a = input("请输入边长a:")
b = input("请输入边长b:")
c = input("请输入边长c:")
a, b, c = int(a), int(b), int(c)
if a > 0 and b > 0 and 0 < c < a + b and a+c > b and c+b > c:
    print("可以组成三角形")
    p = (a+b+c)/2
    area = sqrt(p*(p-a)*(p-b)*(p-c))
    print(F"三角形的面积为：{area:.2f}")
else:
    print("不能组成三角形")
