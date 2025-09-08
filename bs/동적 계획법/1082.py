import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().rstrip().split()))

# 가진 돈
money = int(input())

# n 원으로 만들 수 있는 가장 큰 숫자
# dp[n] n원 만드는데 가장 큰 숫자
dp = [0 for _ in range(money + 1)]
for i in range(1, money + 1):
    for number, price in enumerate(prices):
        # 현재내가 가진 금액으로 숫자를 살 수 있을경우
        if i >= price:
            dp[i] = max(dp[i], int(str(dp[i - price]) + str(number)))
print(dp[money])

