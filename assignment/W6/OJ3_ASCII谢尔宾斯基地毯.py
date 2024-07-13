"""
描述
谢尔宾斯基地毯一种正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均由更小的地毯组成。

现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。

注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应

输入
输入为两行，分别为地毯大小正整数N与组成元素字符串c

输入数据保证N为3的正整数幂
输出
由N行长度为N*len(c)的字符串构成的谢尔宾斯基地毯
样例输入
9
[]
样例输出
[][][][][][][][][]
[]  [][]  [][]  []
[][][][][][][][][]
[][][]      [][][]
[]  []      []  []
[][][]      [][][]
[][][][][][][][][]
[]  [][]  [][]  []
[][][][][][][][][]
"""

N = int(input())
c = input()


def solution(top, left, bottom, square, c):
    if bottom - top < 3:
        return square

    hole_size = (bottom - top + 1) // 3
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                square = make_hole(
                    top + hole_size, left + hole_size, hole_size, square, c
                )
            else:
                square = solution(top + row * hole_size, left + col * hole_size, top + (row + 1) * hole_size, square, c)
    return square

def make_hole(top, left, hole_size, square, c):
    for row in range(top, top + hole_size):
        for col in range(left, left + hole_size):
            square[row][col] = " " * len(c)
    return square


sierpinski_square = solution(0, 0, N - 1, [[c for _ in range(N)] for _ in range(N)], c)
[print("".join(row)) for row in sierpinski_square]
