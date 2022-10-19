#1猜拳游戏
import random #内建函数
choice=['剪刀','石头','布'] #建立一个列表
keepgoing=input('你想出剪刀,石头,布还是(Q)？')
while keepgoing!='Q': #当不回答‘Q'时整个程序会一直执行
    computer=random.choice(choice) #随机选择choice
    print('你选择的是' +keepgoing+ '计算机选择的是' +computer)
#判断输赢
    if keepgoing==computer:
        print('打平了')
    elif keepgoing=='剪刀':
        if computer=='石头':
            print('计算机赢了')
        else:
            print('你赢了')
    elif keepgoing=='石头':
        if computer=='布':
            print('计算机赢了')
        else:
            print('你赢了')
    elif keepgoing=='布':
        if computer=='剪刀':
            print('计算机赢了')
        else:
            print('你赢了')
    else:
        print('你的结果不在范围类！！！')
    print()
    keepgoing=input('你想出剪刀,石头,布还是(Q)？') #继续循环！！！