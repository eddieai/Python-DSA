"""
动态规划解决找零问题的扩展算法
需要得出每种硬币的个数
在生成最优列表的同时跟踪记录所选硬币的币值
得到最后的解后，减去选择的硬币币值，回溯到表格之前的部分找零
"""


def dpMakeChange(coinValueList, change, minCoins):
    usedCoins = [0] * (change + 1)

    for newChange in range(1, change + 1):
        minCoin = None
        usedCoin = None
        for coin in coinValueList:
            if coin > newChange:
                continue
            if minCoin == None or minCoin > 1 + minCoins[newChange - coin]:
                minCoin = 1 + minCoins[newChange - coin]
                usedCoin = coin
        minCoins[newChange] = minCoin
        usedCoins[newChange] = usedCoin

    newChange = change
    changeCoins = []
    while newChange > 0:
        changeCoins.append(usedCoins[newChange])
        newChange -= usedCoins[newChange]

    return minCoins[change], changeCoins, usedCoins


change = 63
print(dpMakeChange([1, 5, 10, 21, 25], change, [0] * (change + 1)))
