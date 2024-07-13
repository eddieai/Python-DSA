"""
描述
如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，可供玩家操作的空间一共只有三根柱子，导致按原传说的要求，需要超过1.8*10^19步才能解开。

透过新增柱子可以大幅度地减少需要的步数。此处要求在给出指定的盘数，柱子数量为4（即限制为4根柱子）且不改变原有传说的其他规则的限制下，找出完成迁移的最小步骤数。

输入
一个非负整数M，M代表盘数，M<=1000。

输出
一个非负整数，表示完成迁移的最小步骤数。

样例输入
3
样例输出
5
"""

M = int(input())

def solution(n_level, from_pole=None, with_pole=None, to_pole=None, n_step=0):
    if n_level == 1:
        print(f"Move disk {1} from {from_pole} to {to_pole}")
        n_step += 1
        return n_step
    if n_level == 2:
        print(f"Move disk {1} from {from_pole} to {with_pole[0]}")
        print(f"Move disk {2} from {from_pole} to {to_pole}")
        print(f"Move disk {1} from {with_pole[0]} to {to_pole}")
        n_step += 3
        return n_step

    n_step = solution(
        n_level - 2, from_pole, [with_pole[1], to_pole], with_pole[0], n_step
    )
    print(f"Move disk {n_level-1} from {from_pole} to {with_pole[1]}")
    print(f"Move disk {n_level} from {from_pole} to {to_pole}")
    print(f"Move disk {n_level-1} from {with_pole[1]} to {to_pole}")
    n_step += 3
    n_step = solution(
        n_level - 2, with_pole[0], [from_pole, with_pole[1]], to_pole, n_step
    )
    return n_step

print(solution(M, from_pole="A", with_pole=["B", "C"], to_pole="D"))
