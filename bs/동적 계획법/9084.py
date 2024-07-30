import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split(" ")))
    money = int(input())

    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, money + 1):
            dp[j] = dp[j] +  dp[j - coin]
    print(dp[money])
