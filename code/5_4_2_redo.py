"""
用递归画分形树
"""

import turtle

t = turtle.Turtle()


def tree(batch_len):
    if batch_len <= 0:
        return
    t.forward(batch_len)
    t.right(20)
    tree(batch_len - 10)
    t.left(40)
    tree(batch_len - 10)
    t.right(20)
    t.backward(batch_len)


t.left(90)  # 保证往上画
t.penup()  # 抬笔
t.backward(100)
t.pendown()
t.pencolor("green")
t.pensize(2)
tree(100)
t.hideturtle()  # 隐藏画笔
turtle.done()
