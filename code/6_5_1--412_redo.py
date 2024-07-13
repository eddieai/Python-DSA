"""
动态规划解大盗宝物问题
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

def dp_thief(tr, max_w):
    m ={(i, w): (0, None) for i in range(len(tr)) for w in range(max_w+1)}

    for i in range(1, len(tr)):
        for w in range(1, max_w+1):
            if tr[i]['w'] > w:
                m[i, w] = m[i-1, w][0], None
            else:
                if m[i-1, w - tr[i]['w']][0] + tr[i]['v'] > m[i-1, w][0]:
                    m[i, w] = m[i-1, w - tr[i]['w']][0] + tr[i]['v'], i
                else:
                    m[i, w] = m[i - 1, w][0], None

    return m[len(tr) - 1, max_w][0], m

max_v, m = dp_thief(tr, max_w)
print(f"Max treasure value = {max_v}")

def print_treasure_list(tr, max_w, m):
    w = max_w
    i = len(tr) - 1
    stolen = []
    while i > 0:
        if m[i, w][1]:
            stolen.append(m[i, w][1])
            w -= tr[i]["w"]
            i -= 1
        else:
            i -= 1
    print(f"Treasure list = {stolen}")
print_treasure_list(tr, max_w, m)

def print_m(tr, max_w, m):
    print(" "*5 + "".join([f"{w:>4}" for w in range(max_w+1)]))
    print((5 + (max_w + 1) * 4) * "-")
    for i in range(len(tr)):
        print_row = f"{i}   |"
        for w in range(max_w+1):
            print_row += f"{m[i, w][0]:>4}"
        print(print_row)
print_m(tr, max_w, m)
