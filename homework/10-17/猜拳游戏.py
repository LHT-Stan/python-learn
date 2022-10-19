import random  # 内建函数
List = ['剪刀', '石头', '布']
keepGoing = input('你想出剪刀,石头,布还是(Q)？')
while keepGoing != 'Q':  # 当不回答‘Q'时整个程序会一直执行
    computer = random.choice(List)  # 随机选择choice
    print('你选择的是' + keepGoing + '计算机选择的是' + computer)
    # 判断输赢
    if keepGoing == computer:
        print('打平了')
    elif keepGoing == '剪刀':
        if computer == '石头':
            print('计算机赢了')
        else:
            print('你赢了')
    elif keepGoing == '石头':
        if computer == '布':
            print('计算机赢了')
        else:
            print('你赢了')
    elif keepGoing == '布':
        if computer == '剪刀':
            print('计算机赢了')
        else:
            print('你赢了')
    else:
        print('你的结果不在范围类！！！')
    print()
    keepGoing = input('你想出剪刀,石头,布还是(Q)？')  # 继续循环！！！
