import turtle as t

# t.pencolor("red")
# t.fillcolor("yellow")
# t.begin_fill()
# for i in range(4):
#    t.fd(100)
#   t.left(90)
# t.end_fill()

def star(x,y):
    t.up() # 拿起画笔
    t.goto(x,y) # 画笔去哪儿
    t.down() # 放下画笔
    t.color("yellow","red") #画笔的颜色
    t.tracer(False) # 关闭动画效果
    t.begin_fill() # 画笔覆盖
    for x in range(5): 
        t.fd(100) # 画笔往前
        t.right(144) # 画笔向右转角度
    t.end_fill() # 结束覆盖颜色
    t.ht() # 画完隐藏乌龟
    t.tracer(True) # 开启动画
    t.done # 双击启动的文件时，执行完成不结束

t.onscreenclick(star, 1) # 点击事件，一个参数对应函数，二个表示鼠标哪个键 
