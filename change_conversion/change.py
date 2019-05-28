# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions without the permission from the author: Shuowei Li(appleearth007@gmail.com),
# (2) you retain this notice, and (3) you provide clear attribution to UC Berkeley, and me.

# this problem is from LeetCode - China, # 332
# see the website: https://leetcode-cn.com/problems/coin-change/

# we assume coins were typed in a sorted order from small to big
# Example: coins = [1, 2, 5], amount = 11
number = 0


def coinChange(coins, amount):
    if len(coins) == 1 and coins[0] < amount:
        return -1
    while coins[len(coins) - 1] > amount:
        coins.pop()
    changeSize = coins[len(coins) - 1]
    global number
    numberLocal = amount // changeSize
    number += amount // changeSize
    coins.pop()
    if len(coins) == 0 or amount - numberLocal * changeSize == 0:
        return number
    return coinChange(coins, amount - numberLocal * changeSize)


# Main Function
if __name__ == '__main__':
    # test1
    lst1 = list([1, 2, 5])
    total1 = 13
    print(coinChange(lst1, total1))

    # test2
    lst2 = list([2])
    total2 = 3
    print(coinChange(lst2, total2))
