import turtle as t


# t.pencolor("red")
# t.fillcolor("yellow")
# t.begin_fill()
# for i in range(4):
#    t.fd(100)
#   t.left(90)
# t.end_fill()

def star(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("yellow", "red")
    t.begin_fill()
    for x in range(5):
        t.fd(100)
        t.right(144)
    t.end_fill()
    t.ht()
