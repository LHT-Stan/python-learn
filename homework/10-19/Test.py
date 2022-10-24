import math

a = int(input("请输入总人数:"))
b = int(input("请输入要分的小组:"))
if a < 0 and b < 0:
    print("输入错误!")
else:
    c = a/b
    print(f"可以分出{math.ceil(c)}个小组")
    





