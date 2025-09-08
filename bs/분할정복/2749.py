import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import defaultdict

dp = defaultdict(int)
dp[0] = 0
dp[1] = 1
dp[2] = 1


def fibo(x):
    if dp.get(x):
        return dp[x] % 1000000
    else:
        if x % 2 == 0:
            dp[x // 2 + 1] = fibo(x // 2 + 1) % 1000000
            dp[x // 2 - 1] = fibo(x // 2 - 1) % 1000000
            return dp[x // 2 + 1] ** 2 - dp[x // 2 - 1] ** 2
        else:
            dp[x//2 + 1] = fibo(x // 2 + 1) % 1000000
            dp[x//2] = fibo(x // 2) % 1000000
            return dp[x // 2 + 1] ** 2 + dp[x // 2] ** 2
x = int(input())
print(fibo(x)% 1000000)