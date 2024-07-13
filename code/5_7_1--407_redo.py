"""
用递归解决动态迷宫
"""
import turtle
from turtle import *
import random
turtle.speed("fastest")

OBSTACLE = "+"
TRIED = "_"  # 面包屑
DeadEnd = "1"  # 验证了是走不通的路
PART_OF_PATH = "G"  # 终点


class Maze:
    def __init__(self, mazeFileName, colorType=None):
        self.colorType = colorType
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazeList = []  # 存储迷宫
        mazeFile = open(mazeFileName, "r")  # 读取迷宫
        for line in mazeFile:
            rowList = []
            col = 0  # 列数
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == "S":
                    self.StartCol = col
                    self.StartRow = rowsInMaze
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazeList.append(rowList)
        columnsInMaze = len(self.mazeList[0])
        print("Loading the Maze successfully\n")

        self.rowsInMaze = rowsInMaze  # 22
        self.columnsInMaze = columnsInMaze  # 20
        self.xTranslate = -columnsInMaze / 2  # -10
        self.yTranslate = rowsInMaze / 2  # 11

        self.t = Turtle(shape="turtle")  # 画图用的海龟

        self.screen = Screen()

        self.screen.setup(width=600, height=600)
        self.screen.setworldcoordinates(
            -(columnsInMaze - 1) / 2 - 0.5,
            -(rowsInMaze - 1) / 2 - 0.5,
            (columnsInMaze - 1) / 2 + 0.5,
            (rowsInMaze - 1) / 2 + 0.5,
        )  # 设置画布的坐标系 (-10,-11) (10,11)

    def drawMaze(self):  # 绘制迷宫
        self.t.speed(10)
        for y in range(self.rowsInMaze):  # 0-22
            for x in range(self.columnsInMaze):  # 0-20
                if self.mazeList[y][x] == OBSTACLE:
                    self.drawCenteredBox(
                        x + self.xTranslate, -y + self.yTranslate
                    )  # 从左上角开始画
                else:  # 画安全区域
                    self.drawCenteredBox(
                        x + self.xTranslate,
                        -y + self.yTranslate,
                        (255 / 255, 250 / 255, 250 / 255),
                    )
        self.t.color(
            "black", (255 / 255, 127 / 255, 80 / 255)
        )  # 画笔颜色和填充颜色 这里是设置的海龟颜色
        print("Have printed the maze")

    def drawCenteredBox(self, x, y, color=None):  # 画迷宫的一个小方块
        # self.screen.tracer(0) # 刷新图片没有延迟
        if self.colorType:  # 使用用户自定的颜色
            self.t.color("black")
            self.t.fillcolor(self.colorType)
        else:  # 用户没有给定则随机颜色
            r = random.randint(100, 130)
            g = random.randint(150, 180)
            self.t.color((r / 255, g / 255, 200 / 255))
        if color:
            self.t.color(color)
        self.t.up()  # 抬起画笔
        self.t.goto(x - 0.5, y - 0.5)
        self.t.setheading(90)  # 设置朝向北
        self.t.down()  # 落笔
        self.t.begin_fill()  # 开始填充
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        self.screen.update()
        self.screen.tracer(1)  # 延迟

    def moveTurtle(self, x, y):  # 把海龟移动到某个位置并且不留下痕迹
        self.t.up()  # 抬笔 避免留下痕迹
        self.t.setheading(
            self.t.towards(x + self.xTranslate, -y + self.yTranslate)
        )  # 找到海龟的朝向
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumble(self, color):  # 洒下面包屑
        self.t.dot(color)

    def updatePosition(self, row, col, val=None):  # 更新海龟的位置并做标注
        if val:
            self.mazeList[row][col] = val
        self.moveTurtle(col, row)  # 把海龟移到新位置
        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DeadEnd:
            color = "orange"
        else:
            color = None
        if color:
            self.dropBreadcrumble(color)

    def isExit(self, row, col):  # 判断是否是出口
        if row == 0 or row == self.rowsInMaze - 1:
            return True
        elif col == 0 or col == -self.columnsInMaze - 1:
            return True
        else:
            return False

    def __getitem__(self, item):
        return self.mazeList[item]  # 让类具有列表查询的功能


def searFrom(maze, startRow, startColum):  # 寻找出口
    if maze[startRow][startColum] == OBSTACLE:
        maze.updatePosition(startRow, startColum, val=OBSTACLE)
        return False
    if maze[startRow][startColum] == TRIED:
        maze.updatePosition(startRow, startColum, val=TRIED)
        return False
    if maze.isExit(startRow, startColum):
        maze.updatePosition(startRow, startColum, val=PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColum, val=TRIED)
    if (
        searFrom(maze, startRow - 1, startColum)
        or searFrom(maze, startRow + 1, startColum)
        or searFrom(maze, startRow, startColum - 1)
        or searFrom(maze, startRow, startColum + 1)
    ):
        maze.updatePosition(startRow, startColum, val=PART_OF_PATH)
        return True
    else:
        maze.updatePosition(startRow, startColum, val=DeadEnd)
        return False


maze = Maze(r"code/5_7_2.txt")
turtle.tracer(0, 0)
maze.drawMaze()
turtle.update()
maze.updatePosition(maze.StartRow, maze.StartCol)
found = searFrom(maze, maze.StartRow, maze.StartCol)
if found:
    print("Find path!")
else:
    print("Failed")
done()
