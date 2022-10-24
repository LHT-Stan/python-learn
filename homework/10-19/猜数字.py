import random
Range = random.randint(1, 100)
number = random.randint(1, Range)
print(f"---电脑已经随机生成1-{Range}之间的整数")
while True:
    guess = int(input("请输入您要猜的数字："))
    if number == guess:
        print("恭喜你猜对了")
        break
    elif number < guess:
        print("您猜的数大了，重新试一下吧")
    elif number > guess:
        print("您猜的数小了，重新试一下吧")
