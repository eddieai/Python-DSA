"""
用递归方法绘制谢尔宾斯基三角形
"""

import turtle


def sierpinski(degree, points):  # degree表示阶数
    if degree < 0:
        return None
    colormap = ["red", "blue", "green", "yellow", "orange", "white"]
    drawTriangle(points, colormap[degree])
    sierpinski(
        degree - 1,
        {
            "left": points["left"],
            "right": getMid(points["left"], points["right"]),
            "top": getMid(points["left"], points["top"]),
        },
    )
    sierpinski(
        degree - 1,
        {
            "left": getMid(points["top"], points["left"]),
            "right": getMid(points["top"], points["right"]),
            "top": points["top"]
        },
    )
    sierpinski(
        degree - 1,
        {
            "left": getMid(points["right"], points["left"]),
            "right": points["right"],
            "top": getMid(points["right"], points["top"]),
        },
    )


def drawTriangle(points, color):  # 填充三角形
    t.fillcolor(color)
    t.penup()
    t.goto(points["top"])
    t.pendown()
    t.begin_fill()
    t.goto(points["left"])
    t.goto(points["right"])
    t.goto(points["top"])
    t.end_fill()


def getMid(p1, p2):  # 找到两个点的中点
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


t = turtle.Turtle()

points = {"left": (-200, -100), "right": (200, -100), "top": (0, 200)}

sierpinski(5, points)

turtle.done()
