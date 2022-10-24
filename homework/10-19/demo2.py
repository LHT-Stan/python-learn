# 例二求已知边长的三角形的面积，结果保留两位小数
# 1.在不清楚三角形高的情况下，可以使用海伦公式计算面积
#   具体公式为s=sqrt(p*(p-a)(p-b)(p-c))
#   假设在平面内，有一个三角形，边长分别为a、b、c，三角形的面积S可由以下公式求得：s=sqrt(p*(p-a)(p-b)(p-c))
#   而公式里的p为半周长（周长的一半）：p=1/2(a+b+c)
# 2.保留两位小数 round(x[,y])按给定精度y返回x的四舍五入值
from math import sqrt
side1, side2, side3 = map(float, input("请输入三角形的三条边：").split())
# 判断是否满足三角形条件
if side1 + side2 > side3:
    # 计算面积
    p = sum([side1, side2, side3])/2
    s = sqrt(p * (p - side1) * (p - side2) * (p - side3))
    # 保留两位小数
    print(f"三角形的面积为{round(s, 2)}")
else:
    print("您输入的无法构成三角形")
