height = float(input("请输入您的身高<米>: "))
weight = float(input("请输入您的体重<公斤>: "))
bmi = weight / (height ** 2)

print("您的BMI指数为：", bmi)
print(type(bmi))
