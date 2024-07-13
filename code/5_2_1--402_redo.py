"""
进制转换的递归方法
"""

def toStr(n, base):  # 转2进制
    base_table = "".join(map(str, range(10))) + "ABCDEF"
    if n < base:
        return base_table[n]
    return toStr(n//base, base) + base_table[n%base]


print(toStr(20, 10))
print(toStr(999, 16))
