"""
递归解大盗宝物问题
"""

# 因为每个宝物只装一次 所以当增加一个重量时，不需要再计算
# 已经装进去的宝物比较大小

tr = [
    None,
    {"w": 2, "v": 3},
    {"w": 3, "v": 4},
    {"w": 4, "v": 8},
    {"w": 5, "v": 8},
    {"w": 9, "v": 10},
]

# 大盗最大承重
max_w = 20

# 初始化m作为记忆化递归的cache
m = {}

def rec_thief(tr_idx, w):
    if tr_idx == set() or w == 0:
        m[tuple(tr_idx), w] = 0
        return 0
    if m.get((tuple(tr_idx), w)):
        return m[tuple(tr_idx), w]

    max_v = 0
    for i in tr_idx:
        if tr[i]["w"] <= w:
            v = rec_thief(tr_idx - set([i]), w - tr[i]["w"]) + tr[i]["v"]
            max_v = max(v, max_v)
    m[tuple(tr_idx), w] = max_v
    return max_v

print(rec_thief(set(range(1, len(tr))), max_w))
