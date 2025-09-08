import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

dp = [0] * 31
dp[1] = 0
dp[2] = 3
dp[3] = 0
dp[4] = 11
for i in range(5, n+1):
    if i % 2:
        dp[i] = 0
    else:
        dp[i] = dp[i-2] * 3 + dp[i-2] - dp[i-4]
print(dp[n])