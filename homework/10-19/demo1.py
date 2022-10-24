# 班级分组
# 采用向上取整
# 输入班级人数
from math import ceil

num1, num2 = map(int, input("请输入班级总人数和需要分几组的数字。（用空格隔开即可）").split())
if num1 > num2:
    print(f"可以分"+str(ceil(num1/num2))+"组")
if num1 < num2:
    print(f"可以分"+str(ceil(num2/num1))+"组")
if num1 % num2 != 0:
    print(f"其中有{num1 % num2}个人为一组")
