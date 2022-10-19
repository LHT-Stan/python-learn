# a = int(input("请输入一个整数: "))
# b = int(input("请输入一个整数: "))
# if a > b:  # 如果第一个数大于第二数
#     a, b = b, a   # 交换两个数
# print(a, b)



x = input("请输入两个以空格隔开的整数: ")
a, b = map(int, x.split())
if a > b:  # 如果第一个数大于第二数
    a, b = b, a   # 交换两个数
print(a, b)
