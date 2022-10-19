import random as rd


def printNum(num):
    if num == 1:
        str = "石头"
    elif num == 2:
        str = "剪刀"
    elif num == 3:
        str = "布"
    return str


num = 0

com = rd.randint(1, 3)

while num < 4:
    num = int(input("请输入一个数开始猜拳游戏（1-石头，2-剪刀，3-布，4-结束游戏）\n"))
    print("您出的是:", printNum(num), ",电脑出的是:", printNum(com))
    if (num == 1 and com == 2) or (num == 2 and com == 3) or (num == 3 and com == 1):
        print("恭喜您，获得胜利")
    elif num == com:
        print("打平了哦")
    else:
        print("很遗憾，您输了")
