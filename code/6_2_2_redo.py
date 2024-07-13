"""
用递归解决找零问题
"""


def recDC(coinValueList, change, knnowResults):
    if knnowResults[change] != 0:
        return knnowResults[change]
    if change in coinValueList:
        return 1

    n_coin = []
    for coin in coinValueList:
        if coin > change:
            break
        n_coin.append(recDC(coinValueList, change - coin, knnowResults) + 1)
    n_coin = min(n_coin)
    knnowResults[change] = n_coin
    return n_coin


change = 63
print(recDC([1, 5, 10, 21, 25], change, [0] * (change+1)))
