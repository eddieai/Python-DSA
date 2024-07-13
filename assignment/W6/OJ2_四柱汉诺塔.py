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

n_step_cache = [None for _ in range(M+1)]

def hanoi4(k):
    if n_step_cache[k]:
        return n_step_cache[k]

    if k == 1:
        n_step_cache[1] = 1
    elif k == 2:
        n_step_cache[2] = 3
    else:
        n_step = []
        for i in range(1, k):
            n_step.append(2 * hanoi4(i) + 2 ** (k-i) - 1)
        n_step_cache[k] = min(n_step)

    return n_step_cache[k]

print(hanoi4(M))
