"""
十进制转为16进制以下的任意进制
"""

from pythonds.basic.stack import Stack

def baseConvert(decNumber, base):
    digits = "0123456789ABCDEF"
    remain = Stack()

    while decNumber > 0:
        remain.push(digits[decNumber % base])
        decNumber = decNumber // base

    res = []
    while not remain.isEmpty():
        res.append(remain.pop())

    return "".join(res)

print(baseConvert(25, 2))