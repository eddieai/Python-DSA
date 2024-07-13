"""
动态规划解决找零问题
"""


def dpMakeChange(coinValueList, change):
    minCoins = [0] * (change + 1)
    for newChange in range(1, change+1):
        minCoin = None
        for coin in coinValueList:
            if coin > newChange:
                continue
            if minCoin == None or minCoin > 1 + minCoins[newChange - coin]:
                minCoin = 1 + minCoins[newChange - coin]
        minCoins[newChange] = minCoin

    return minCoins[change]


change = 63
print(dpMakeChange([1, 5, 10, 21, 25], change))
