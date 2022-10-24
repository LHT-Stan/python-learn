import random
Range = random.randint(1, 100)
number = random.randint(1, Range)
print(f"---电脑已经随机生成1-{Range}之间的整数")
y = "y"
Y = "Y"
n = "n"
N = "N"
while True:
    # 模拟电脑随机生成1~100的整数
    # 设置猜的次数
    guess = int(input(f"请输入1-{Range}以内的整数："))
    if guess > number:
        print("你猜大了")
        s = input("是否继续游戏y/n")
        if s is y or s is Y:
            pass
        elif s is n or s is N:
            break
    elif guess < number:
        print("你猜小了")
        s = input("是否继续游戏y/n")
        if s is y or s is Y:
            pass
        elif s is n or s is N:
            break
    else:
        print("恭喜你赢了")
        break

