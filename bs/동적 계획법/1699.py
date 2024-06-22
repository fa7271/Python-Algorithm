import math
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

dp = [1e9 for i in range(n+1)]

for i in range(1, n + 1):
    # 제곱근인 경우
    if math.isqrt(i) ** 2 == i:
        dp[i] = 1
    else:
        for j in range(1, int(i ** 0.5) + 1):
            if dp[i] > (dp[i - j * j] + 1):
                dp[i] = dp[i - j * j] + 1
print(dp[n])
