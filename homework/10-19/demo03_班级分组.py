from math import ceil
a, b = map(int, input("请依次输入班级人数以及需要分的小组数（以空格隔开）：").split())
c = ceil(a/b)
d = a % b
print(f"有{c}组，其中有{d}名同学额外一组")

