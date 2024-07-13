"""
用递归画螺旋
"""

import turtle

t = turtle.Turtle()


def drawSpiral(t, linelen):
    if linelen <= 0:
        return
    t.forward(linelen)
    t.right(90)
    drawSpiral(t, linelen - 5)
    return


drawSpiral(t, 100)
print("done")
turtle.done()
