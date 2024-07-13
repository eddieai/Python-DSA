"""
递归
数列求和
"""

def listsum(numList):
    print(numList)
    if len(numList) == 1:
        print(numList[0])
        return numList[0]

    res = listsum(numList[1:]) + numList[0]
    # res = numList[0] + listsum(numList[1:])
    print(res)
    return res

print(listsum([1, 3, 5, 7, 9]))
